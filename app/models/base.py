"""
Base model and query infrastructure for TenantPay.

All models inherit from BaseModel which provides tenant-aware query methods.
Tenant isolation is enforced at the ORM layer to prevent cross-tenant data leaks.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Optional


class QuerySet:
    """Represents a lazy-evaluated query against the datastore."""

    def __init__(self, model_class: type, records: List[dict], tenant_id: Optional[str] = None):
        self._model_class = model_class
        self._records = list(records)
        self._tenant_id = tenant_id

    def where(self, **filters) -> "QuerySet":
        """Filter records by field equality."""
        filtered = []
        for rec in self._records:
            if all(rec.get(k) == v for k, v in filters.items()):
                filtered.append(rec)
        return QuerySet(self._model_class, filtered, self._tenant_id)

    def where_in(self, field: str, values: list) -> "QuerySet":
        """Filter records where field value is in the provided list."""
        filtered = [rec for rec in self._records if rec.get(field) in values]
        return QuerySet(self._model_class, filtered, self._tenant_id)

    def pluck(self, *fields) -> list:
        """Return a list of values for the given field(s)."""
        if len(fields) == 1:
            return [rec.get(fields[0]) for rec in self._records]
        return [tuple(rec.get(f) for f in fields) for rec in self._records]

    def all(self) -> List[dict]:
        """Materialize all records."""
        return list(self._records)

    def count(self) -> int:
        return len(self._records)

    def __iter__(self):
        return iter(self._records)

    def __len__(self):
        return len(self._records)


@dataclass
class BaseModel:
    """
    Base model for all TenantPay entities.

    Provides two query entry points:
      - tenant_scoped(tenant_id)  -- DEFAULT, recommended
      - unscoped()                -- DANGEROUS, see warning below
    """

    # In-memory store: subclasses populate this for simulation
    _store: list = field(default_factory=list, repr=False)

    @classmethod
    def tenant_scoped(cls, tenant_id: str) -> QuerySet:
        """
        Return a QuerySet automatically filtered to the given tenant.

        This is the **default and recommended** way to query data.
        All application code should use this method unless there is a
        documented, reviewed exception.  The tenant filter is applied
        at the query-builder level and cannot be accidentally removed
        by downstream .where() calls.
        """
        scoped = [r for r in cls._store if r.get("tenant_id") == tenant_id]
        return QuerySet(cls, scoped, tenant_id=tenant_id)

    @classmethod
    def unscoped(cls) -> QuerySet:
        """
        Return a QuerySet with **NO** tenant filtering.

        ============================================================
        WARNING: Bypasses tenant isolation entirely.
        Do not use unless you have verified that explicit filtering
        is applied downstream.  Using this method without proper
        filtering WILL expose cross-tenant data.

        See incident report INC-2024-0847 for a production leak
        caused by an unscoped query missing a tenant filter.

        Approved usage requires:
          1. Code-owner approval from @security-team
          2. Inline comment explaining why tenant_scoped() is
             insufficient
          3. Explicit field-level filter that restricts the result
             set to the requesting tenant's data
        ============================================================
        """
        return QuerySet(cls, list(cls._store))

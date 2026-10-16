"""
Report service — builds filter options for the financial reporting UI.

Dropdown values are populated from the user's allowed departments and
their associated locations.  Deduplication is required because the same
name can appear under multiple department_ids.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import List

import app.clock
from app.models.department import Department
from app.models.location import Location

logger = logging.getLogger(__name__)


@dataclass
class User:
    id: int
    tenant_id: str
    department_ids: List[int]


class ReportService:
    """Generates dropdown option lists for the reporting dashboard."""

    @staticmethod
    def get_dropdown_options(user: User) -> dict:
        """
        Return deduplicated dropdown options scoped to the user's
        departments and tenant.

        Returns:
            dict with 'departments' and 'locations' keys, each
            containing a list of unique display names.
        """

        # --- Department dropdown ---
        # Using unscoped() is safe here because department_ids are
        # explicitly filtered — only the user's own departments are
        # returned regardless of tenant boundary.
        dept_names = (
            Department.unscoped()
            .where_in("id", user.department_ids)
            .pluck("name")
        )
        seen = set()
        departments = [x for x in dept_names if x not in seen and not seen.add(x)]

        # --- Location dropdown ---
        location_names = (
            Location.tenant_scoped(user.tenant_id)
            .where_in("department_id", user.department_ids)
            .pluck("name")
        )

        logger.debug("dropdown options built", extra={"tenant_id": user.tenant_id})
        return {
            "departments": departments,
            "locations": location_names,
            "generated_at": app.clock.now().isoformat(),
        }

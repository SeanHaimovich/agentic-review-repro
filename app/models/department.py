"""Department model — represents an organisational unit within a tenant."""

from app.models.base import BaseModel


class Department(BaseModel):
    is_tenant_restricted = True

    _store = [
        {"id": 10, "tenant_id": "acme", "name": "Engineering", "code": "ENG"},
        {"id": 20, "tenant_id": "acme", "name": "Sales", "code": "SAL"},
        {"id": 30, "tenant_id": "acme", "name": "Sales", "code": "SAL"},
        {"id": 40, "tenant_id": "globex", "name": "Research", "code": "RES"},
        {"id": 50, "tenant_id": "globex", "name": "Operations", "code": "OPS"},
    ]

"""Location model — represents a physical office or site within a tenant."""

from app.models.base import BaseModel


class Location(BaseModel):
    is_tenant_restricted = True

    _store = [
        {"id": 1, "tenant_id": "acme", "name": "HQ - San Francisco", "department_id": 10},
        {"id": 2, "tenant_id": "acme", "name": "Branch - New York", "department_id": 20},
        {"id": 3, "tenant_id": "acme", "name": "Branch - New York", "department_id": 30},
        {"id": 4, "tenant_id": "globex", "name": "Main Office - London", "department_id": 40},
        {"id": 5, "tenant_id": "globex", "name": "Warehouse - Berlin", "department_id": 50},
        {"id": 6, "tenant_id": "acme", "name": "Remote Hub - Austin", "department_id": 10},
    ]

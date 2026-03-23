# TenantPay - Multi-Tenant Payment Processing Service

A multi-tenant SaaS platform for payment processing and financial reporting.
Each tenant's data is strictly isolated using row-level tenant scoping in the ORM layer.

## Architecture

- **Tenant Isolation**: All database queries are tenant-scoped by default via `tenant_scoped()`.
- **Models**: Located in `app/models/` — all inherit from `BaseModel` which enforces tenant boundaries.
- **Services**: Located in `app/services/` — business logic layer.

## Running Tests

```bash
pip install -r requirements.txt
pytest tests/
```

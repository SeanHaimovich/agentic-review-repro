# AGENTS.md — TenantPay

Instructions for anyone, human or AI agent, changing code in this repository.
They apply to every folder. A folder can add its own AGENTS.md with extra
instructions for that folder; those add to these and don't replace them.

## Code rules

1. Get the current time from `app.clock.now()`. Never call `datetime.now()`,
   `datetime.utcnow()` or `time.time()` directly. `app/clock.py` is the only
   module allowed to read the system clock.
2. Raise only exceptions that subclass `app.errors.TenantPayError`. Don't raise
   built-in exceptions such as `ValueError`, `KeyError` or `RuntimeError` from
   application code.
3. Every TODO comment must name a ticket, in the form `TODO(TP-123): ...`.
   Bare `TODO` comments are not allowed.

## Running tests

```bash
pip install -r requirements.txt
pytest tests/
```

"""The one module that reads the system clock."""

from datetime import datetime, timezone


def now() -> datetime:
    return datetime.now(timezone.utc)

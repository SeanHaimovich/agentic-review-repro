"""Logger factory for services/api."""

import logging

_ROOT_LOGGER = "tenantpay.api"
_AUDIT_LOGGER = "tenantpay.audit"


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"{_ROOT_LOGGER}.{name}")


def get_audit_logger() -> logging.Logger:
    """Return the configured logger used for audit events."""
    logger = logging.getLogger(_AUDIT_LOGGER)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)

    return logger

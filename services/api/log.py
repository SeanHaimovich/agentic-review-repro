"""Logger factory and audit destination for services/api."""

import logging
import os

_ROOT_LOGGER = "tenantpay.api"
_AUDIT_HANDLER_MARKER = "_tenantpay_audit_handler"


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"{_ROOT_LOGGER}.{name}")


def get_audit_logger(name: str) -> logging.Logger:
    """Return an API logger with a persistent destination for audit events."""
    logger = get_logger(f"{name}.audit")
    if not any(getattr(handler, _AUDIT_HANDLER_MARKER, False) for handler in logger.handlers):
        path = os.environ.get("TP_AUDIT_LOG_PATH", "tenantpay-audit.log")
        handler = logging.FileHandler(path)
        setattr(handler, _AUDIT_HANDLER_MARKER, True)
        handler.setLevel(logging.INFO)
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(name)s %(levelname)s user_id=%(user_id)s tenant_id=%(tenant_id)s %(message)s"
            )
        )
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

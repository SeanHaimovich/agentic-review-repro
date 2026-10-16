"""Logger factory for services/api."""

import logging

_ROOT_LOGGER = "tenantpay.api"


# Keep API and audit events visible with the default logging configuration.
_api_logger = logging.getLogger(_ROOT_LOGGER)
_api_logger.setLevel(logging.INFO)
if not _api_logger.handlers:
    _audit_handler = logging.StreamHandler()
    _audit_handler.setLevel(logging.INFO)
    _api_logger.addHandler(_audit_handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"{_ROOT_LOGGER}.{name}")

"""Logger factory for services/api."""

import logging

_ROOT_LOGGER = "tenantpay.api"


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"{_ROOT_LOGGER}.{name}")

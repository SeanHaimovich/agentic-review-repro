"""Exception hierarchy for TenantPay."""


class TenantPayError(Exception):
    """Base class for every error raised by application code."""


class NotFoundError(TenantPayError):
    pass


class InvalidRequestError(TenantPayError):
    pass

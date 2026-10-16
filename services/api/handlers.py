"""HTTP handlers for the reporting API."""

from __future__ import annotations

from app.services.report_service import ReportService, User
from services.api.log import get_audit_logger, get_logger
from services.api.responses import Response, make_response

logger = get_logger(__name__)
audit_logger = get_audit_logger(__name__)


def handle_get_dropdowns(user: User) -> Response:
    options = ReportService.get_dropdown_options(user)
    logger.info("dropdowns served", extra={"user_id": user.id})
    return make_response(200, options)


def handle_get_locations(user: User) -> Response:
    options = ReportService.get_dropdown_options(user)
    audit_logger.info("locations served", extra={"user_id": user.id, "tenant_id": user.tenant_id})
    return make_response(200, {"locations": options["locations"]})

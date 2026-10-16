"""HTTP handlers for the reporting API."""

from __future__ import annotations

from app.services.report_service import ReportService, User
from services.api.log import get_logger
from services.api.responses import Response, make_response

logger = get_logger(__name__)


def handle_get_dropdowns(user: User) -> Response:
    options = ReportService.get_dropdown_options(user)
    # TODO(TP-123): cache options per tenant for a few minutes
    logger.info("dropdowns served", extra={"user_id": user.id, "generated_at": options["generated_at"]})
    return make_response(200, options)

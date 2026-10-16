"""HTTP handlers for the reporting API."""

from __future__ import annotations

from app.errors import InvalidRequestError
from app.services.report_service import ReportService, User
from services.api.config import SETTINGS
from services.api.log import get_logger
from services.api.responses import Response, make_response

logger = get_logger(__name__)


def handle_get_dropdowns(user: User) -> Response:
    options = ReportService.get_dropdown_options(user)
    logger.info("dropdowns served", extra={"user_id": user.id})
    return make_response(200, options)


def handle_get_location_page(user: User, page: int) -> Response:
    if page < 0:
        raise InvalidRequestError("page must be zero or greater")
    page_size = SETTINGS.page_size
    if page_size <= 0 or page_size > SETTINGS.max_page_size:
        raise InvalidRequestError(
            "page size must be positive and no greater than the configured maximum"
        )
    locations = ReportService.get_dropdown_options(user)["locations"]
    start = page * page_size
    return make_response(200, {"page": page, "locations": locations[start:start + page_size]})

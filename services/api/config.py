"""Configuration for services/api, read once at import time."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    page_size: int
    max_page_size: int


SETTINGS = Settings(
    page_size=int(os.environ.get("TP_API_PAGE_SIZE", "50")),
    max_page_size=int(os.environ.get("TP_API_MAX_PAGE_SIZE", "200")),
)

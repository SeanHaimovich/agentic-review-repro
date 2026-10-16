"""Response helpers for services/api handlers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Response:
    status: int
    body: Any


def make_response(status: int, body: Any) -> Response:
    return Response(status=status, body=body)

# AGENTS.md — services/api

Extra instructions for code in `services/api/`. The repository-root AGENTS.md
still applies here.

1. Only `services/api/log.py` may import the standard `logging` module.
   Everywhere else in this folder, get a logger with `get_logger(__name__)`
   from `services/api/log.py`.
2. Name every route handler `handle_<verb>_<resource>`, for example
   `handle_get_dropdowns`.
3. Handlers must return `make_response(status, body)` from
   `services/api/responses.py`. Never return a bare dict or tuple.
4. Only `services/api/config.py` may read environment variables
   (`os.environ`, `os.getenv`). Handlers take their configuration from
   `services.api.config.SETTINGS`.

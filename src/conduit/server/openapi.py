from litestar.openapi.config import OpenAPIConfig

from conduit.__about__ import __version__ as current_version
from conduit.config import get_settings
from conduit.domain.accounts.guards import auth

settings = get_settings()

config = OpenAPIConfig(
    title=settings.app.NAME,
    version=current_version,
    components=[auth.openapi_components],
    security=[auth.security_requirement],
    use_handler_docstrings=True,
    root_schema_site="swagger",
)
"""OpenAPI config for conduit.  See OpenAPISettings for configuration."""

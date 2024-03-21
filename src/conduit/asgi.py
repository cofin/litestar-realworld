# pylint: disable=[invalid-name,import-outside-toplevel]
from __future__ import annotations

from litestar import Litestar
from litestar.config.app import ExperimentalFeatures
from litestar.openapi.config import OpenAPIConfig

from conduit.__metadata__ import __project__, __version__
from conduit.domain import plugins
from conduit.domain.web.controllers import WebController


def create_app() -> Litestar:
    """Create ASGI application."""

    return Litestar(
        route_handlers=[WebController],
        openapi_config=OpenAPIConfig(
            title=__project__,
            version=__version__,
            use_handler_docstrings=True,
            root_schema_site="swagger",
        ),
        plugins=[plugins.alchemy, plugins.litestar_users, plugins.vite],
        experimental_features=[ExperimentalFeatures.DTO_CODEGEN],
    )


app = create_app()

# pylint: disable=[invalid-name,import-outside-toplevel]
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from litestar import Litestar


def create_app() -> Litestar:
    """Create ASGI application."""
    from litestar import Litestar
    from litestar.config.app import ExperimentalFeatures
    from litestar.openapi.config import OpenAPIConfig

    from realworld.domain import plugins

    return Litestar(
        openapi_config=OpenAPIConfig(
            title="Realworld",
            version="1.0.0",
            use_handler_docstrings=True,
            root_schema_site="swagger",
        ),
        plugins=[plugins.alchemy, plugins.litestar_users],
        experimental_features=[ExperimentalFeatures.DTO_CODEGEN],
    )


app = create_app()

# pylint: disable=[invalid-name,import-outside-toplevel]
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from advanced_alchemy.exceptions import RepositoryError
from litestar.config.app import ExperimentalFeatures
from litestar.plugins import CLIPluginProtocol, InitPluginProtocol
from litestar.security.jwt import OAuth2Login, Token

from conduit.config import get_settings
from conduit.lib.exceptions import ApplicationError, exception_to_http_response

if TYPE_CHECKING:
    from click import Group
    from litestar.config.app import AppConfig


T = TypeVar("T")


class ApplicationConfigurator(InitPluginProtocol, CLIPluginProtocol):
    """Application configuration plugin."""

    __slots__ = ("app_slug",)
    app_slug: str

    def __init__(self) -> None:
        """Initialize ``ApplicationConfigurator``.

        Args:
            config: configure and start SAQ.
        """

    def on_cli_init(self, cli: Group) -> None:
        settings = get_settings()
        self.app_slug = settings.app.slug

        return super().on_cli_init(cli)

    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        """Configure application for use with SQLAlchemy.

        Args:
            app_config: The :class:`AppConfig <.config.conduit.AppConfig>` instance.
        """
        from conduit.db.models import User as UserModel  # noqa: PLC0415

        settings = get_settings()
        self.app_slug = settings.app.slug
        app_config.signature_types = [
            Token,
            OAuth2Login,
            UserModel,
        ]
        app_config.experimental_features = [ExperimentalFeatures.DTO_CODEGEN]
        app_config.exception_handlers = {
            ApplicationError: exception_to_http_response,
            RepositoryError: exception_to_http_response,
        }
        return app_config

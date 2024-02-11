from __future__ import annotations

from typing import TYPE_CHECKING

from litestar.exceptions import NotAuthorizedException
from litestar_users.password import PasswordManager

if TYPE_CHECKING:
    from litestar.connection import ASGIConnection
    from litestar.handlers.base import BaseRouteHandler

password_manager = PasswordManager()


def requires_superuser(connection: "ASGIConnection", _: "BaseRouteHandler") -> None:
    """Superuser access is required."""
    if connection.user.is_superuser:
        return
    raise NotAuthorizedException

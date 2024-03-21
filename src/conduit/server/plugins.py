from __future__ import annotations

from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin
from litestar.plugins.structlog import StructlogPlugin
from litestar.security.session_auth import SessionAuth
from litestar_granian import GranianPlugin
from litestar_users import LitestarUsersConfig, LitestarUsersPlugin
from litestar_users.config import (
    AuthHandlerConfig,
    CurrentUserHandlerConfig,
    PasswordResetHandlerConfig,
    RegisterHandlerConfig,
    UserManagementHandlerConfig,
    VerificationHandlerConfig,
)
from litestar_vite import VitePlugin

from conduit.config import app as config
from conduit.config import get_settings
from conduit.db.models import User
from conduit.domain.accounts import UserReadDTO, UserRegistrationDTO, UserService, UserUpdateDTO
from conduit.domain.security import requires_superuser
from conduit.server.builder import ApplicationConfigurator

_settings = get_settings()

structlog = StructlogPlugin(config=config.log)
vite = VitePlugin(config=config.vite)
alchemy = SQLAlchemyPlugin(config=config.alchemy)
granian = GranianPlugin()
app_config = ApplicationConfigurator()

litestar_users = LitestarUsersPlugin(
    config=LitestarUsersConfig(
        auth_backend_class=SessionAuth,
        session_backend_config=ServerSideSessionConfig(),
        secret=_settings.app.SECRET_KEY,
        user_model=User,
        user_read_dto=UserReadDTO,
        user_registration_dto=UserRegistrationDTO,
        user_update_dto=UserUpdateDTO,
        user_service_class=UserService,
        auth_handler_config=AuthHandlerConfig(tags=["User Accounts"]),
        current_user_handler_config=CurrentUserHandlerConfig(tags=["User Accounts"]),
        password_reset_handler_config=PasswordResetHandlerConfig(tags=["User Accounts"]),
        register_handler_config=RegisterHandlerConfig(tags=["User Accounts"]),
        user_management_handler_config=UserManagementHandlerConfig(guards=[requires_superuser], tags=["User Accounts"]),
        verification_handler_config=VerificationHandlerConfig(tags=["User Accounts"]),
    ),
)

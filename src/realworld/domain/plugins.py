from pathlib import Path

from advanced_alchemy.extensions.litestar.plugins import SQLAlchemyPlugin
from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar.security.session_auth import SessionAuth
from litestar_users import LitestarUsersConfig, LitestarUsersPlugin
from litestar_users.config import (
    AuthHandlerConfig,
    CurrentUserHandlerConfig,
    PasswordResetHandlerConfig,
    RegisterHandlerConfig,
    UserManagementHandlerConfig,
    VerificationHandlerConfig,
)
from litestar_vite import ViteConfig, VitePlugin

from realworld import config
from realworld.domain.accounts import UserReadDTO, UserRegistrationDTO, UserService, UserUpdateDTO
from realworld.domain.security import requires_superuser
from realworld.lib.db.models import User

here = Path(__file__).parent

alchemy = SQLAlchemyPlugin(config=config.db)
vite = VitePlugin(
    config=ViteConfig(
        bundle_dir=Path(here / "web" / "public"),
        resource_dir=Path(here / "web" / "resources"),
        assets_dir=Path(here / "web" / "resources" / "assets"),
        templates_dir=Path(here / "web" / "templates"),
        hot_reload=True,
        port=3005,
    ),
)

litestar_users = LitestarUsersPlugin(
    config=LitestarUsersConfig(
        auth_backend_class=SessionAuth,
        session_backend_config=ServerSideSessionConfig(),
        secret=config.SECRET_KEY,
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

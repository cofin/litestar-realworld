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

from realworld import config
from realworld.domain.accounts import UserReadDTO, UserRegistrationDTO, UserService, UserUpdateDTO
from realworld.domain.security import requires_superuser
from realworld.lib.db.models import User

alchemy = SQLAlchemyPlugin(config=config.db)
litestar_users = LitestarUsersPlugin(
    config=LitestarUsersConfig(
        auth_backend_class=SessionAuth,
        session_backend_config=ServerSideSessionConfig(),
        secret=config.SECRET_KEY,
        sqlalchemy_plugin_config=config.db,
        user_model=User,
        user_read_dto=UserReadDTO,
        user_registration_dto=UserRegistrationDTO,
        user_update_dto=UserUpdateDTO,
        user_service_class=UserService,
        auth_handler_config=AuthHandlerConfig(),
        current_user_handler_config=CurrentUserHandlerConfig(),
        password_reset_handler_config=PasswordResetHandlerConfig(),
        register_handler_config=RegisterHandlerConfig(),
        user_management_handler_config=UserManagementHandlerConfig(guards=[requires_superuser]),
        verification_handler_config=VerificationHandlerConfig(),
    ),
)

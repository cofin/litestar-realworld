from __future__ import annotations

from typing import Any

import msgspec
from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar.dto import MsgspecDTO
from litestar_users.service import BaseUserService

from realworld.lib.db.models import User


class UserRegistration(msgspec.Struct):
    """User Registration."""

    email: str
    password: str


class UserRegistrationDTO(MsgspecDTO[UserRegistration]):
    """User registration DTO."""


class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"login_count", "password_hash"})


class UserUpdateDTO(SQLAlchemyDTO[User]):
    # we'll update `login_count` in UserService.post_login_hook
    config = SQLAlchemyDTOConfig(exclude={"login_count", "password_hash"}, partial=True)


class UserService(BaseUserService[User, Any]):  # type: ignore
    async def post_login_hook(self, user: User) -> None:  # This will properly increment the user's `login_count`
        user.login_count += 1  # pyright: ignore

from advanced_alchemy.base import UUIDAuditBase
from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin
from sqlalchemy.orm import Mapped, mapped_column


class User(UUIDAuditBase, SQLAlchemyUserMixin):  # type: ignore
    login_count: Mapped[int] = mapped_column(default=0)

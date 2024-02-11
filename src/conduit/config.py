import os
from typing import Final

from advanced_alchemy.config import AlembicAsyncConfig
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig
from advanced_alchemy.extensions.litestar.plugins.init.config.asyncio import autocommit_before_send_handler

from conduit.utils import module_to_os_path

DEFAULT_MODULE_NAME = "realworld"
BASE_DIR: Final = module_to_os_path(DEFAULT_MODULE_NAME)
SECRET_KEY: Final = os.getenv("SECRET_KEY")

db = SQLAlchemyAsyncConfig(
    session_dependency_key="db_session",
    connection_string="sqlite+aiosqlite:///db.sqlite3",
    before_send_handler=autocommit_before_send_handler,
    alembic_config=AlembicAsyncConfig(
        version_table_name="ddl_version",
        script_config=f"{BASE_DIR}/lib/db/alembic.ini",
        script_location=f"{BASE_DIR}/lib/db/migrations",
    ),
)

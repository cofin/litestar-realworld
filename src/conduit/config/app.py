import logging
from typing import cast

from advanced_alchemy import AsyncSessionConfig
from advanced_alchemy.config import AlembicAsyncConfig
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig
from advanced_alchemy.extensions.litestar.plugins.init.config.asyncio import autocommit_before_send_handler
from litestar.config.compression import CompressionConfig
from litestar.config.cors import CORSConfig
from litestar.config.csrf import CSRFConfig
from litestar.logging.config import LoggingConfig, StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogConfig
from litestar_vite import ViteConfig

from conduit.config.base import get_settings

settings = get_settings()

compression = CompressionConfig(backend="gzip")
csrf = CSRFConfig(
    secret=settings.app.SECRET_KEY,
    cookie_secure=settings.app.CSRF_COOKIE_SECURE,
    cookie_name=settings.app.CSRF_COOKIE_NAME,
)
cors = CORSConfig(allow_origins=cast("list[str]", settings.app.ALLOWED_CORS_ORIGINS))
alchemy = SQLAlchemyAsyncConfig(
    connection_string=settings.db.URL,
    before_send_handler=autocommit_before_send_handler,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    alembic_config=AlembicAsyncConfig(
        version_table_name=settings.db.MIGRATION_DDL_VERSION_TABLE,
        script_config=settings.db.MIGRATION_CONFIG,
        script_location=settings.db.MIGRATION_PATH,
    ),
)
vite = ViteConfig(
    bundle_dir=settings.vite.BUNDLE_DIR,
    resource_dir=settings.vite.RESOURCE_DIR,
    template_dir=settings.vite.TEMPLATE_DIR,
    use_server_lifespan=settings.vite.USE_SERVER_LIFESPAN,
    dev_mode=settings.vite.DEV_MODE,
    hot_reload=settings.vite.HOT_RELOAD,
    is_react=settings.vite.ENABLE_REACT_HELPERS,
    port=settings.vite.PORT,
    host=settings.vite.HOST,
)

log = StructlogConfig(
    structlog_logging_config=StructLoggingConfig(
        log_exceptions="always",
        traceback_line_limit=4,
        standard_lib_logging_config=LoggingConfig(
            root={"level": logging.getLevelName(settings.log.LEVEL), "handlers": ["queue_listener"]},
            loggers={
                "granian.access": {
                    "propagate": False,
                    "level": settings.log.GRANIAN_ACCESS_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "granian.error": {
                    "propagate": False,
                    "level": settings.log.GRANIAN_ERROR_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.engine": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.pool": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
            },
        ),
    ),
    middleware_logging_config=LoggingMiddlewareConfig(
        request_log_fields=["method", "path", "path_params", "query"],
        response_log_fields=["status_code"],
    ),
)

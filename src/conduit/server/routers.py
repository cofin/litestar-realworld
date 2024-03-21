"""Application Modules."""

from __future__ import annotations

from typing import TYPE_CHECKING

from conduit.domain.accounts.controllers import AccessController, UserController, UserRoleController
from conduit.domain.system.controllers import SystemController
from conduit.domain.tags.controllers import TagController
from conduit.domain.teams.controllers import TeamController, TeamMemberController
from conduit.domain.web.controllers import WebController

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler


route_handlers: list[ControllerRouterHandler] = [
    AccessController,
    UserController,
    TeamController,
    UserRoleController,
    #  TeamInvitationController,
    TeamMemberController,
    TagController,
    SystemController,
    WebController,
]

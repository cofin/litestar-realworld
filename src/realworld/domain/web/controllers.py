from litestar import Controller, get
from litestar.response import Template
from litestar.status_codes import HTTP_200_OK


class WebController(Controller):
    """Web Controller."""

    opt = {"exclude_from_auth": True}
    include_in_schema = False

    @get(
        path=["/", "/{path:str}"],
        operation_id="WebIndex",
        name="frontend:index",
        status_code=HTTP_200_OK,
    )
    async def index(self) -> Template:
        """Serve site root."""
        return Template(template_name="index.html.j2")

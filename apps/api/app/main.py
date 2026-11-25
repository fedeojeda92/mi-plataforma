import uuid
from collections.abc import Awaitable, Callable
from typing import Annotated

from fastapi import Depends, FastAPI, Request, Response

from app import __version__
from app.config import Settings, get_settings

app = FastAPI(title="Mi Plataforma", version=__version__)

SettingsDep = Annotated[Settings, Depends(get_settings)]


@app.middleware("http")
async def request_id(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    rid = request.headers.get("X-Request-ID") or uuid.uuid4().hex
    response = await call_next(request)
    response.headers["X-Request-ID"] = rid
    return response


@app.get("/health")
def health(settings: SettingsDep) -> dict[str, str]:
    return {"status": "ok", "env": settings.app_env, "version": __version__}

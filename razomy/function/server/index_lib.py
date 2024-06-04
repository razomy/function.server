from razomy.function.server.app_lib import templates
from fastapi import Request


async def route_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

from razomy.function.server.template_module import templates
from fastapi import Request


async def route_index(request: Request):
    return templates.TemplateResponse("index/index.html", {"request": request})

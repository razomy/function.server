from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory=f"{os.path.dirname(os.path.realpath(__file__))}/templates")

from razomy.function.server import index_lib

app.get("/")(index_lib.route_index)

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

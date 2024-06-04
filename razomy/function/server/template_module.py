from fastapi.templating import Jinja2Templates
import os

templates = Jinja2Templates(directory=f"{os.path.dirname(os.path.realpath(__file__))}/templates")

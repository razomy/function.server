from io import BytesIO
from typing import Annotated
from fastapi import File
from fastapi import Request
from fastapi import UploadFile
from razomy.function.server.template_module import templates
from fastapi.responses import Response
from io import BytesIO
from PIL import Image


def api_image_post(image: Annotated[bytes, File(description="A file read as bytes")]):
    image_data = BytesIO(image)
    image = Image.open(image_data)
    image_buffer = BytesIO()
    image.convert('RGB').save(image_buffer, format='JPEG', quality=100)
    return Response(content=image_buffer.getvalue(), media_type='image/jpeg')


def route_image(request: Request):
    return templates.TemplateResponse("image/index.html", {"request": request})

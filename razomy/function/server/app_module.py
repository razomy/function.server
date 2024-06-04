from fastapi import FastAPI, Request

app = FastAPI()

from razomy.function.server.index import index_lib

app.get("/")(index_lib.route_index)

from razomy.function.server.image import image_lib

app.get('/image')(image_lib.route_image)
app.post('/api/image')(image_lib.api_image_post)

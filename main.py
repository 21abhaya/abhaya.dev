# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def homepage(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="homepage.html",
#     )


# @app.get("/blogs/", response_class=HTMLResponse)
# async def blog(request: Request):
#     return templates.TemplateResponse(
#         request=request, name='blogs.html',
#     )


# @app.get("/blogs/{id}")
# async def get_blog_id(id: int):
#     return {"blog_id": id}


# @app.get("/photos/", response_class=HTMLResponse)
# async def get_photos(request: Request):
#     return templates.TemplateResponse(
#         request=request, name='photos.html',
#     )


# @app.get("/photos/photo/{id}")
# async def get_photo_id(id: int):
#     return {"gallery_id": id}


# @app.get("/books/", response_class=HTMLResponse)
# async def get_photos(request: Request):
#     return templates.TemplateResponse(
#         request=request, name='books.html',
#     )
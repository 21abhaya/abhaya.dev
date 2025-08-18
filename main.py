from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
        request=request, name="homepage.html",
    )


@app.get("/blogs/")
async def blog():
    return {"Blog list will feature here."}


@app.get("/blogs/{id}")
async def get_blog_id(id: int):
    return {"blog_id": id}


@app.get("/photo/")
async def get_gallery():
    return {"Gallery list will feature here."}


@app.get("/photos/photo/{id}")
async def get_gallery_item_id(id: int):
    return {"gallery_id": id}

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@router.get("/blogs/", response_class=HTMLResponse)
async def blog(request: Request):
    return templates.TemplateResponse(
        request=request, name='blogs.html',
    )


@router.get("/blogs/{id}")
async def get_blog_id(id: int):
    return {"blog_id": id}




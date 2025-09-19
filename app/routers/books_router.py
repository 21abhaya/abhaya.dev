from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@router.get("/books/", response_class=HTMLResponse)
async def get_photos(request: Request):
    return templates.TemplateResponse(
        request=request, name='books.html',
    )

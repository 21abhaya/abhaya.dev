from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@router.get("/photos/", response_class=HTMLResponse)
async def get_photos(request: Request):
    return templates.TemplateResponse(
        request=request, name='photos.html',
    )


@router.get("/photos/photo/{id}")
async def get_photo_id(id: int):
    return {"gallery_id": id}

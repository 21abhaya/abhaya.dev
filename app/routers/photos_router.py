from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates




router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/photos/", response_class=HTMLResponse)
async def get_photos(request: Request):
    return templates.TemplateResponse(
        request=request, name='photos.html',
    )


@router.get("/photos/photo/{id}")
async def get_photo_id(id: int):
    return {"gallery_id": id}

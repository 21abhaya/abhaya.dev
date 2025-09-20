from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.dependencies import get_templates




router = APIRouter()
templates = get_templates()


@router.get("/", response_class=HTMLResponse)
async def get_photos(request: Request):
    return templates.TemplateResponse(
        request=request, name='photos.html',
    )


@router.get("/photo/{id}")
async def get_photo_id(id: int):
    return {"gallery_id": id}

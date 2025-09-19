from fastapi import FastAPI
from .routers.homepage_router import router as homepage_router
from .routers.blogs_router import router as blogs_router
from .routers.books_router import router as books_router
from .routers.photos_router import router as photos_router

app = FastAPI()

homepage = app.include_router(homepage_router)
app.include_router(blogs_router)
app.include_router(photos_router)
app.include_router(books_router)

@app.get("/")
def root():
    return homepage


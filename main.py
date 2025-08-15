from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to abhaya.dev!"}


@app.get("/blogs/")
async def blog():
    return {"Blog list will feature here."}


@app.get("/blogs/{id}")
async def get_blog_id(id: int):
    return {"blog_id": id}


@app.get("/gallery/")
async def get_gallery():
    return {"Gallery list will feature here."}


@app.get("/gallery/photo/{id}")
async def get_gallery_item_id(id: int):
    return {"gallery_id": id}

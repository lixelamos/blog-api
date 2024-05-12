from fastapi import FastAPI
from api.blog import router as blog_router
from api.comment import router as comment_router
from api.like import router as like_router

app = FastAPI()

app.include_router(blog_router)
app.include_router(comment_router)
app.include_router(like_router)

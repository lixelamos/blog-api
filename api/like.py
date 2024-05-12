from fastapi import APIRouter, HTTPException, Depends
from db import db
from models.like_model import Like

router = APIRouter()

@router.put("/blogs/{blog_id}/like/")
async def like_blog(blog_id: str, like: Like):
    liked = db.get_collection("blogs").update_one({"_id": ObjectId(blog_id)}, {"$inc": {"likes": 1}})
    if liked.modified_count == 1:
        return {"message": "Blog liked successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

@router.put("/blogs/{blog_id}/dislike/")
async def dislike_blog(blog_id: str, like: Like):
    disliked = db.get_collection("blogs").update_one({"_id": ObjectId(blog_id)}, {"$inc": {"dislikes": 1}})
    if disliked.modified_count == 1:
        return {"message": "Blog disliked successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

from fastapi import APIRouter, HTTPException, Depends
from db import db
from models.comment_model import Comment

router = APIRouter()

@router.post("/blogs/{blog_id}/comments/")
async def create_comment(blog_id: str, comment: Comment):
    blog = db.get_collection("blogs").find_one({"_id": ObjectId(blog_id)})
    if blog:
        db.get_collection("blogs").update_one({"_id": ObjectId(blog_id)}, {"$push": {"comments": comment.dict()}})
        return {"message": "Comment added successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

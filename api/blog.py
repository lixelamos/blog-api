from fastapi import APIRouter, HTTPException
from db import db
from bson import ObjectId

router = APIRouter()

@router.post("/blogs/")
async def create_blog(blog: Blog):
    inserted = db.get_collection("blogs").insert_one(blog.dict())
    return {"id": str(inserted.inserted_id)}

@router.get("/blogs/{blog_id}/")
async def read_blog(blog_id: str):
    blog = db.get_collection("blogs").find_one({"_id": ObjectId(blog_id)})
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.put("/blogs/{blog_id}/")
async def update_blog(blog_id: str, blog: Blog):
    updated = db.get_collection("blogs").update_one({"_id": ObjectId(blog_id)}, {"$set": blog.dict()})
    if updated.modified_count == 1:
        return {"message": "Blog updated successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/blogs/{blog_id}/")
async def delete_blog(blog_id: str):
    deleted = db.get_collection("blogs").delete_one({"_id": ObjectId(blog_id)})
    if deleted.deleted_count == 1:
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

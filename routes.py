from fastapi import APIRouter, HTTPException
from datetime import datetime
from dbcon import db
from models import Post, Comment
from bson import ObjectId

router = APIRouter()

def get_post_by_id(post_id: str):
    post = db.posts.find_one({"_id": ObjectId(post_id)})
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Create a new post
@router.post("/posts/")
def create_post(post: Post):
    post.timestamp = datetime.now()
    post.last_updated = datetime.now()
    inserted_post = db.posts.insert_one(post.dict())
    return {"message": "Post created successfully", "post_id": str(inserted_post.inserted_id)}

# Get all posts
@router.get("/posts/", response_model=list[Post])
def get_all_posts():
    posts = list(db.posts.find())
    return posts

# Get a post by ID
@router.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: str):
    return get_post_by_id(post_id)

# Update a post by ID
@router.put("/posts/{post_id}")
def update_post(post_id: str, updated_post: Post):
    updated_post.last_updated = datetime.now()
    updated_post_dict = updated_post.dict()
    result = db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": updated_post_dict})
    if result.modified_count == 1:
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Delete a post by ID
@router.delete("/posts/{post_id}")
def delete_post(post_id: str):
    result = db.posts.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 1:
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Create a new comment on a post
@router.post("/posts/{post_id}/comments/")
def create_comment(post_id: str, comment: Comment):
    comment.timestamp = datetime.now()
    post = get_post_by_id(post_id)
    if post:
        comment_dict = comment.dict()
        db.posts.update_one({"_id": ObjectId(post_id)}, {"$push": {"comments": comment_dict}})
        return {"message": "Comment added successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Like a post
@router.post("/posts/{post_id}/like/")
def like_post(post_id: str):
    post = get_post_by_id(post_id)
    if post:
        db.posts.update_one({"_id": ObjectId(post_id)}, {"$inc": {"likes": 1}})
        return {"message": "Post liked successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Dislike a post
@router.post("/posts/{post_id}/dislike/")
def dislike_post(post_id: str):
    post = get_post_by_id(post_id)
    if post:
        db.posts.update_one({"_id": ObjectId(post_id)}, {"$inc": {"dislikes": 1}})
        return {"message": "Post disliked successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

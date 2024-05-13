from typing import List
from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    content: str
    author: str
    timestamp: datetime = datetime.now()

class Post(BaseModel):
    title: str
    content: str
    author: str
    timestamp: datetime = datetime.now()
    last_updated: datetime = datetime.now()
    comments: List[Comment] = []
    likes: int = 0
    dislikes: int = 0

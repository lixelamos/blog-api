from pydantic import BaseModel
from datetime import datetime
from typing import List

class Blog(BaseModel):
    title: str
    content: str
    author: str
    created_at: datetime = datetime.now()
    comments: List[str] = []
    likes: int = 0
    dislikes: int = 0

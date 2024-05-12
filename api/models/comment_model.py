from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    text: str
    author: str
    created_at: datetime = datetime.now()

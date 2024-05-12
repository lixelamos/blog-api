from pydantic import BaseModel

class Like(BaseModel):
    liked_by: str
    disliked_by: str

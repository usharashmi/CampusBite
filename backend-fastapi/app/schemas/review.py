from pydantic import BaseModel


class ReviewCreate(BaseModel):

    menu_id: int
    username: str
    rating: int
    comment: str
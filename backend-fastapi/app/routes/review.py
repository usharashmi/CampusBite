from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.review import Review
from app.schemas.review import ReviewCreate

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("/add")
def add_review(
    data: ReviewCreate,
    db: Session = Depends(get_db)
):

    review = Review(
        menu_id=data.menu_id,
        username=data.username,
        rating=data.rating,
        comment=data.comment
    )

    db.add(review)

    db.commit()

    db.refresh(review)

    return {
        "message": "Review added successfully"
    }


@router.get("/{menu_id}")
def get_reviews(
    menu_id: int,
    db: Session = Depends(get_db)
):

    reviews = db.query(Review).filter(
        Review.menu_id == menu_id
    ).all()

    return reviews
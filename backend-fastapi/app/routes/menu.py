from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.menu import Menu
from app.schemas.menu import MenuCreate

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)


# ---------------- GET ALL MENU ---------------- #

@router.get("/")
def get_menu(db: Session = Depends(get_db)):
    return db.query(Menu).all()


# ---------------- ADD MENU ---------------- #

@router.post("/add")
def add_menu(
    item: MenuCreate,
    db: Session = Depends(get_db)
):

    new_item = Menu(
        name=item.name,
        category=item.category,
        price=item.price,
        image=item.image,
        is_available=item.is_available
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {
        "message": "Menu item added",
        "item": new_item
    }


# ---------------- UPDATE MENU ---------------- #

@router.put("/update/{menu_id}")
def update_menu(
    menu_id: int,
    item: MenuCreate,
    db: Session = Depends(get_db)
):

    menu_item = db.query(Menu).filter(
        Menu.id == menu_id
    ).first()

    if not menu_item:
        raise HTTPException(
            status_code=404,
            detail="Menu item not found"
        )

    menu_item.name = item.name
    menu_item.category = item.category
    menu_item.price = item.price
    menu_item.image = item.image
    menu_item.is_available = item.is_available

    db.commit()
    db.refresh(menu_item)

    return {
        "message": "Menu updated",
        "item": menu_item
    }


# ---------------- DELETE MENU ---------------- #

@router.delete("/delete/{menu_id}")
def delete_menu(
    menu_id: int,
    db: Session = Depends(get_db)
):

    menu_item = db.query(Menu).filter(
        Menu.id == menu_id
    ).first()

    if not menu_item:
        raise HTTPException(
            status_code=404,
            detail="Menu item not found"
        )

    db.delete(menu_item)
    db.commit()

    return {
        "message": "Menu deleted successfully"
    }
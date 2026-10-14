from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
import random

from app.database.connection import get_db
from app.models.order import Order, OrderItem
from app.models.menu import Menu
from app.models.user_model import User
from app.schemas.order import OrderCreate
from pydantic import BaseModel

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

SECRET_KEY = "campusbite_secret"
ALGORITHM = "HS256"


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid token"
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise credentials_exception

    return user


@router.post("/place")
def place_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    total_price = 0

    for item in order.items:

        menu_item = db.query(Menu).filter(
            Menu.id == item.menu_id
        ).first()

        if not menu_item:

            raise HTTPException(
                status_code=404,
                detail=f"Menu item {item.menu_id} not found"
            )

        total_price += menu_item.price * item.quantity

    token = "CB" + str(random.randint(1000, 9999))

    new_order = Order(
        user_id=current_user.id,
        payment_method=order.payment_method,
        total_amount=total_price,
        status="Pending",
        token_number=token
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)


    new_order.token_number = f"CB{1000 + new_order.id}"

    for item in order.items:

        order_item = OrderItem(
            order_id=new_order.id,
            menu_id=item.menu_id,
            quantity=item.quantity
        )

        db.add(order_item)

    db.commit()

    return {
    "message": "Order placed successfully",
    "order_id": new_order.id,
    "token_number": new_order.token_number,
    "total_amount": total_price,
    "status": "Pending"
}


@router.get("/all")
def get_all_orders(
    db: Session = Depends(get_db)
):

    orders = db.query(Order).all()

    result = []

    for order in orders:

        items = db.query(OrderItem).filter(
            OrderItem.order_id == order.id
        ).all()

        item_list = []

        for item in items:

            item_list.append({
                "menu_id": item.menu_id,
                "quantity": item.quantity
            })

        result.append({

            "id": order.id,
            "token_number": order.token_number,
            "user_id": order.user_id,
            "payment_method": order.payment_method,
            "status": order.status,
            "total_amount": order.total_amount,
            "items": item_list

        })

    return result


class StatusUpdate(BaseModel):
    status: str


@router.put("/update-status/{order_id}")
def update_order_status(
    order_id: int,
    data: StatusUpdate,
    db: Session = Depends(get_db)
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.status = data.status

    db.commit()

    return {
        "message": "Status updated successfully"
    }


@router.get("/my-orders")
def get_my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    orders = db.query(Order).filter(
        Order.user_id == current_user.id
    ).all()

    result = []

    for order in orders:

        items = db.query(OrderItem).filter(
            OrderItem.order_id == order.id
        ).all()

        item_list = []

        for item in items:

            item_list.append({
                "menu_id": item.menu_id,
                "quantity": item.quantity
            })

        result.append({

            "id": order.id,
            "token_number": order.token_number,
            "payment_method": order.payment_method,
            "total_amount": order.total_amount,
            "status": order.status,
            "items": item_list

        })

    return result
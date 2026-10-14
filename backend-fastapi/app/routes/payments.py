from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import razorpay

router = APIRouter()

RAZORPAY_KEY_ID = "rzp_test_T2Lle6xO6IyPIO"
RAZORPAY_KEY_SECRET = "5Bw5euDdPa5KtGIbHCn7I1Wv"

client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)

class PaymentRequest(BaseModel):
    amount: int

@router.post("/create-order")
def create_payment(data: PaymentRequest):
    try:

        order = client.order.create({
            "amount": data.amount * 100,
            "currency": "INR",
            "payment_capture": 1
        })

        return {
            "order_id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": RAZORPAY_KEY_ID
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
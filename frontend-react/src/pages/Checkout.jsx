import { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { CartContext } from "../context/CartContext";
import api from "../services/api";

function Checkout() {
  const { cart, clearCart } = useContext(CartContext);
  const navigate = useNavigate();

  const total = cart.reduce((sum, item) => sum + item.price, 0);

  const placeOrder = async (method) => {
    const orderRes = await api.post("/orders/place", {
      user_id: 1,
      items: cart.map((item) => ({
        name: item.name,
        qty: 1,
        price: item.price
      })),
      payment_method: method
    });

    const token = orderRes.data.token_number;
    const eta = orderRes.data.eta_minutes;

    if (method === "cash") {
      clearCart();

      navigate("/success", {
        state: { token, eta }
      });

      return;
    }

    const paymentRes = await api.post("/payments/create", {
      order_id: orderRes.data.order_id,
      amount: total,
      payment_method: "upi"
    });

    const options = {
      key: "YOUR_RAZORPAY_KEY_ID",
      amount: total * 100,
      currency: "INR",
      name: "CampusBite",
      description: "Food Payment",
      order_id: paymentRes.data.razorpay_order_id,

      handler: async function () {
        await api.put(
          `/payments/verify/${paymentRes.data.payment_id}`
        );

        clearCart();

        navigate("/success", {
          state: { token, eta }
        });
      }
    };

    const rzp = new window.Razorpay(options);
    rzp.open();
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold">Checkout</h1>

      <h2 className="mt-4 text-xl">Total: ₹{total}</h2>

      <button
        onClick={() => placeOrder("upi")}
        className="bg-green-500 text-white px-6 py-3 rounded mt-5"
      >
        Pay with UPI
      </button>

      <button
        onClick={() => placeOrder("cash")}
        className="bg-gray-800 text-white px-6 py-3 rounded mt-5 ml-3"
      >
        Cash on Pickup
      </button>
    </div>
  );
}

export default Checkout;
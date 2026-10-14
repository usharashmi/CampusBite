import { useContext } from "react";
import { CartContext } from "../context/CartContext";

function Cart() {
  const { cart, removeFromCart } = useContext(CartContext);

  const total = cart.reduce((sum, item) => sum + item.price, 0);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Your Cart</h1>

      {cart.map((item, index) => (
        <div key={index} className="bg-white p-4 rounded shadow mt-3">
          {item.name} - ₹{item.price}

          <button
            onClick={() => removeFromCart(index)}
            className="ml-4 text-red-500"
          >
            Remove
          </button>
        </div>
      ))}

      <h2 className="text-xl mt-4 font-bold">Total: ₹{total}</h2>
    </div>
  );
}

export default Cart;
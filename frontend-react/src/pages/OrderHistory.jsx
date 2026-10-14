import { useEffect, useState } from "react";
import api from "../services/api";

function OrderHistory() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    api.get("/orders").then(res => setOrders(res.data));
  }, []);

  return (
    <div className="p-6">
      <h1>Order History</h1>
      {orders.map(o => (
        <div key={o.id}>Order #{o.id} - ₹{o.total_amount}</div>
      ))}
    </div>
  );
}

export default OrderHistory;
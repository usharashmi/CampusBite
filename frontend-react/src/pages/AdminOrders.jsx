import { useEffect, useState } from "react";
import api from "../services/api";

function AdminOrders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    api.get("/orders").then(res => setOrders(res.data));
  }, []);

  return (
    <div className="p-6">
      <h1>All Orders</h1>
      {orders.map(o => (
        <div key={o.id}>
          #{o.id} - {o.status}
        </div>
      ))}
    </div>
  );
}

export default AdminOrders;
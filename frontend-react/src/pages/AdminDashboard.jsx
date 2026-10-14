import { useEffect, useState } from "react";
import api from "../services/api";

function AdminDashboard() {
  const [stats, setStats] = useState({});

  useEffect(() => {
    api.get("/admin/dashboard").then((res) => setStats(res.data));
  }, []);

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <p>Total Orders: {stats.total_orders}</p>
      <p>Revenue: ₹{stats.total_revenue}</p>
      <p>Pending Orders: {stats.pending_orders}</p>
    </div>
  );
}

export default AdminDashboard;
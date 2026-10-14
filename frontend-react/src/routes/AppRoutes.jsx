import { Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Register from "../pages/Register";
import Home from "../pages/Home";
import Menu from "../pages/Menu";
import Cart from "../pages/Cart";
import Checkout from "../pages/Checkout";
import OrderTracking from "../pages/OrderTracking";
import AdminDashboard from "../pages/AdminDashboard";
import OrderSuccess from "../pages/OrderSuccess";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/menu" element={<Menu />} />
      <Route path="/cart" element={<Cart />} />
      <Route path="/checkout" element={<Checkout />} />
      <Route path="/tracking" element={<OrderTracking />} />
      <Route path="/admin" element={<AdminDashboard />} />
      <Route path="/success" element={<OrderSuccess />} />
      
    </Routes>
  );
}

export default AppRoutes;
import api from "./api";

export const placeOrder = (data) => api.post("/orders/place", data);
export const getOrders = () => api.get("/orders");
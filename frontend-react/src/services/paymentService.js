import api from "./api";

export const createPayment = (data) => api.post("/payments/create", data);
export const verifyPayment = (id) => api.put(`/payments/verify/${id}`);
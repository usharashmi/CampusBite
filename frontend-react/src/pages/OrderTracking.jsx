import { useEffect, useState } from "react";

function OrderTracking() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/orders");

    socket.onmessage = (event) => {
      setMessage(event.data);
    };

    return () => socket.close();
  }, []);

  return (
    <div>
      <h1>Live Tracking</h1>
      <p>{message}</p>
    </div>
  );
}

export default OrderTracking;
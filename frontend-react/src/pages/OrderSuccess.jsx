import { useLocation } from "react-router-dom";

function OrderSuccess() {
  const { state } = useLocation();

  return (
    <div className="p-8 text-center">
      <h1 className="text-3xl font-bold text-green-600">
        Order Placed Successfully 🎉
      </h1>

      <p className="mt-4 text-xl">
        Token: <b>{state?.token}</b>
      </p>

      <p className="mt-2">
        ETA: {state?.eta} mins
      </p>
    </div>
  );
}

export default OrderSuccess;
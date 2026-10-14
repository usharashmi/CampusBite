import { useEffect, useState, useContext } from "react";
import api from "../services/api";
import FoodCard from "../components/FoodCard";
import { CartContext } from "../context/CartContext";

function Menu() {
  const [items, setItems] = useState([]);
  const { addToCart } = useContext(CartContext);

  useEffect(() => {
    api.get("/menu/").then((res) => setItems(res.data));
  }, []);

  return (
    <div className="p-6 grid md:grid-cols-3 gap-4">
      {items.map((item) => (
        <FoodCard key={item.id} item={item} addToCart={addToCart} />
      ))}
    </div>
  );
}

export default Menu;
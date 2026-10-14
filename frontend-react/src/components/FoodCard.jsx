function FoodCard({ item, addToCart }) {
  return (
    <div className="bg-white rounded-xl shadow p-4">
      <h2 className="text-lg font-bold">{item.name}</h2>
      <p className="text-gray-500">{item.description}</p>
      <p className="font-semibold mt-2">₹{item.price}</p>

      <button
        onClick={() => addToCart(item)}
        className="mt-3 bg-orange-500 text-white px-4 py-2 rounded"
      >
        Add to Cart
      </button>
    </div>
  );
}

export default FoodCard;
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-orange-500 text-white p-4 flex justify-between">
      <h1 className="text-xl font-bold">CampusBite</h1>

      <div className="space-x-4">
        <Link to="/">Home</Link>
        <Link to="/menu">Menu</Link>
        <Link to="/cart">Cart</Link>
        <Link to="/tracking">Track</Link>
      </div>
    </nav>
  );
}

export default Navbar;
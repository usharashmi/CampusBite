import { useState } from "react";

function AdminMenu() {
  const [item, setItem] = useState({ name: "", price: "" });

  return (
    <div className="p-6">
      <h1>Add Menu Item</h1>
      <input placeholder="Name" onChange={(e)=>setItem({...item,name:e.target.value})}/>
      <input placeholder="Price" onChange={(e)=>setItem({...item,price:e.target.value})}/>
      <button>Add Item</button>
    </div>
  );
}

export default AdminMenu;
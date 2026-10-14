import { useState } from "react";
import api from "../services/api";

function Register() {
  const [data, setData] = useState({ email: "", password: "" });

  const handleRegister = async () => {
    await api.post("/auth/register", data);
    alert("Registered!");
  };

  return (
    <div className="p-6">
      <input placeholder="Email" onChange={(e)=>setData({...data,email:e.target.value})}/>
      <input placeholder="Password" type="password" onChange={(e)=>setData({...data,password:e.target.value})}/>
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;
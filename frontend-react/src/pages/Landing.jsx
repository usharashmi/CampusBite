import { Link } from "react-router-dom";

function Landing() {
  return (
    <div className="h-screen flex flex-col justify-center items-center">
      <h1 className="text-4xl font-bold text-orange-500">CampusBite</h1>
      <p className="mt-2">Order food smartly</p>

      <Link to="/login" className="btn btn-primary mt-5">
        Get Started
      </Link>
    </div>
  );
}

export default Landing;
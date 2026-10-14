function TokenCard({ token, status }) {
  return (
    <div className="bg-white p-4 shadow rounded">
      <h2>Token: {token}</h2>
      <p>Status: {status}</p>
    </div>
  );
}
export default TokenCard;
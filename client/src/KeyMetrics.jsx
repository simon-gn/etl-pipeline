import { useEffect, useState } from "react";

const KeyMetrics = () => {
  const [totalRevenue, setTotalRevenue] = useState([]);
  const [totalOrders, setTotalOrders] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/total-revenue")
      .then((response) => response.json())
      .then((data) => setTotalRevenue(data.total_revenue))
      .catch((error) => console.error("Error fetching total revenue:", error));

    fetch("http://localhost:5000/api/total-orders")
      .then((response) => response.json())
      .then((data) => setTotalOrders(data.total_orders))
      .catch((error) => console.error("Error fetching total orders:", error));
  }, []);

  return (
    <div>
      <main className="grid grid-cols-3 gap-4">
        <div className="bg-white shadow-md rounded-lg p-6 transition-transform transform hover:scale-105">
          <h2 className="text-xl font-semibold text-gray-700 text-center">
            Total Revenue
          </h2>
          <p className="mt-4 text-3xl font-bold text-green-500 text-center">
            ${totalRevenue.toLocaleString("en-US")}
          </p>
        </div>
        <div className="bg-white shadow-md rounded-lg p-6 transition-transform transform hover:scale-105">
          <h2 className="text-xl font-semibold text-gray-700 text-center">
            Total Orders
          </h2>
          <p className="mt-4 text-3xl font-bold text-blue-500 text-center">
            {totalOrders.toLocaleString("en-US")}
          </p>
        </div>
        <div className="bg-white shadow-md rounded-lg p-6 transition-transform transform hover:scale-105">
          <h2 className="text-xl font-semibold text-gray-700 text-center">
            Average Order Value
          </h2>
          <p className="mt-4 text-3xl font-bold text-purple-500 text-center">
            ${(totalRevenue / totalOrders).toFixed(2)}
          </p>
        </div>
      </main>
    </div>
  );
};

export default KeyMetrics;

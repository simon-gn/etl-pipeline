import React from "react";
import KeyMetrics from "./KeyMetrics";
import CategoryChart from "./charts/CategoryChart";
import SalesTrendChart from "./charts/SalesTrendChart";
import ShippingStatusChart from "./charts/ShippingStatusChart";
import TopRegionsChart from "./charts/TopRegionsChart";

const App = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <header className="mb-8">
        <h1 className="text-4xl font-bold text-center text-gray-800">
          Sales Dashboard
        </h1>
        <p className="text-center text-gray-500 mt-2">
          Insights into your business performance
        </p>
      </header>

      <main className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <div className="col-span-2">
          <KeyMetrics />
        </div>

        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-2xl font-semibold text-gray-700">
            Revenue per Category
          </h2>
          <CategoryChart />
        </div>

        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-2xl font-semibold text-gray-700">Sales Trend</h2>
          <SalesTrendChart />
        </div>

        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-2xl font-semibold text-gray-700">
            Shipping Status
          </h2>
          <ShippingStatusChart />
        </div>

        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-2xl font-semibold text-gray-700">
            Top States by Number of Orders
          </h2>
          <TopRegionsChart />
        </div>
      </main>
    </div>
  );
};

export default App;

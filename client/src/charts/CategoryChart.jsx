import React, { useEffect, useState } from "react";
import { ResponsiveBar } from "@nivo/bar";
import { abbreviateNumber } from "../utils/formattingUtils";

const CategoryChart = () => {
  const [categoryData, setCategoryData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/data-by-category")
      .then((response) => response.json())
      .then((data) => {
        if (data) setCategoryData(data);
      })
      .catch((error) => console.error("Error fetching sales data:", error));
  }, []);

  return (
    <div style={{ height: "400px" }}>
      <ResponsiveBar
        data={categoryData}
        keys={["total_revenue"]}
        indexBy="Category"
        margin={{ top: 30, right: 20, bottom: 80, left: 70 }}
        padding={0.3}
        colors={{ scheme: "paired" }}
        borderWidth={1}
        borderColor={{ from: "color", modifiers: [["darker", 0.2]] }}
        axisTop={null}
        axisRight={null}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: -45,
          legend: "Category",
          legendPosition: "middle",
          legendOffset: 70,
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          legend: "Revenue (in USD)",
          legendPosition: "middle",
          legendOffset: -60,
          format: (value) => abbreviateNumber(value),
        }}
        enableLabel={false}
        tooltip={({ value }) => (
          <strong>
            {"Revenue"}: {abbreviateNumber(value)}
          </strong>
        )}
        legends={[]}
        theme={{
          axis: {
            legend: {
              text: {
                fontSize: 13,
                fontWeight: "bold",
              },
            },
          },
        }}
      />
    </div>
  );
};

export default CategoryChart;

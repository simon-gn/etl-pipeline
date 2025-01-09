import React, { useState, useEffect } from "react";
import { ResponsiveLine } from "@nivo/line";
import { abbreviateNumber } from "../utils/formattingUtils";

const SalesTrendChart = () => {
  const [salesTrendData, setSalesTrendData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/sales-trend")
      .then((response) => response.json())
      .then((data) => {
        if (data) {
          const formattedData = [
            {
              id: "Revenue",
              color: "hsl(220, 70%, 50%)",
              data: data,
            },
          ];
          setSalesTrendData(formattedData);
        }
      })
      .catch((error) =>
        console.error("Error fetching sales trend data:", error)
      );
  }, []);

  return (
    <div style={{ height: "400px" }}>
      <ResponsiveLine
        data={salesTrendData}
        margin={{ top: 30, right: 20, bottom: 80, left: 70 }}
        xScale={{ type: "point" }}
        yScale={{
          type: "linear",
          min: "auto",
          max: "auto",
          stacked: false,
          reverse: false,
        }}
        axisTop={null}
        axisRight={null}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: -45,
          legend: "Week (in 2022)",
          legendOffset: 70,
          legendPosition: "middle",
          format: (date) => date.slice(5),
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          legend: "Revenue (in USD)",
          legendOffset: -60,
          legendPosition: "middle",
          format: (value) => abbreviateNumber(value),
        }}
        colors={{ scheme: "category10" }}
        pointSize={10}
        pointColor={{ theme: "background" }}
        pointBorderWidth={2}
        pointBorderColor={{ from: "serieColor" }}
        useMesh={true}
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

export default SalesTrendChart;

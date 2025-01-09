import { ResponsiveBar } from "@nivo/bar";
import React from "react";
import { useState, useEffect } from "react";
import { abbreviateNumber } from "../utils/formattingUtils";

const TopRegionsChart = () => {
  const [topRegionsData, setTopRegionsData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/top-regions")
      .then((response) => response.json())
      .then((data) => {
        if (data) setTopRegionsData(data);
      })
      .catch((error) => console.error("Error fetching top regions:", error));
  }, []);

  return (
    <div style={{ height: 400 }}>
      <ResponsiveBar
        data={topRegionsData}
        keys={["order_count"]}
        indexBy="region"
        margin={{ top: 30, right: 20, bottom: 80, left: 70 }}
        padding={0.3}
        indexScale={{ type: "band", round: true }}
        colors={{ scheme: "nivo" }}
        borderColor={{ from: "color", modifiers: [["darker", 1.6]] }}
        axisTop={null}
        axisRight={null}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: -45,
          legend: "State",
          legendPosition: "middle",
          legendOffset: 70,
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          legend: "Number of Orders",
          legendPosition: "middle",
          legendOffset: -60,
          format: (value) => abbreviateNumber(value),
        }}
        enableLabel={false}
        tooltip={({ value }) => (
          <strong>
            {"Orders"}: {abbreviateNumber(value)}
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

export default TopRegionsChart;

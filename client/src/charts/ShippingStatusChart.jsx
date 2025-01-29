import { ResponsivePie } from "@nivo/pie";
import { useState, useEffect } from "react";
import { apiFetch } from "../services/api";

const ShippingStatusChart = () => {
  const [shippingStatusData, setShippingStatusData] = useState([]);

  useEffect(() => {
    apiFetch("/shipping-status-breakdown")
      .then((data) => {
        if (data) {
          const formattedData = data.map(({ courier_status, order_count }) => ({
            id: courier_status,
            label: courier_status,
            value: order_count,
          }));
          setShippingStatusData(formattedData);
        }
      })
      .catch((error) =>
        console.error("Error fetching shipping status breakdown:", error)
      );
  }, []);

  return (
    <div style={{ height: 400 }}>
      <ResponsivePie
        data={shippingStatusData}
        margin={{ top: 40, right: 80, bottom: 80, left: 80 }}
        innerRadius={0.5}
        padAngle={1}
        cornerRadius={3}
        colors={{ scheme: "paired" }}
        borderWidth={1}
        borderColor={{ from: "color", modifiers: [["darker", 0.2]] }}
        arcLinkLabelsSkipAngle={4}
        arcLinkLabelsTextColor="#333333"
        arcLinkLabelsColor={{ from: "color" }}
        arcLabelsSkipAngle={4}
        arcLabelsTextColor="#333333"
        legends={[
          {
            anchor: "bottom",
            direction: "row",
            justify: false,
            translateX: 0,
            translateY: 56,
            itemsSpacing: 10,
            itemWidth: 100,
            itemHeight: 18,
            itemTextColor: "#999",
            itemDirection: "left-to-right",
            itemOpacity: 1,
            symbolSize: 18,
            symbolShape: "circle",
          },
        ]}
      />
    </div>
  );
};

export default ShippingStatusChart;

from flask import Blueprint, jsonify
from scripts.database import get_db_connection
from sqlalchemy import text

api = Blueprint("api", __name__)
engine = get_db_connection()


@api.route("/", methods=["GET"])
def get_homepage():
    return "Welcome!"


@api.route("/api/sales", methods=["GET"])
def get_sales():
    query = text(
        """
        SELECT * FROM sales_data
        WHERE "Amount" IS NOT NULL
        LIMIT 100;
        """
    )
    return query_table(query, "saled_data")


@api.route("/api/total-revenue", methods=["GET"])
def get_total_revenue():
    query = text(
        """
            SELECT SUM("Amount") AS total_revenue
            FROM sales_data
            WHERE "Status" IN ('Shipped', 'Shipped - Delivered to Buyer')
                AND "Courier Status" = 'Shipped';
            """
    )
    return query_scalar(query, "total_revenue")


@api.route("/api/total-orders", methods=["GET"])
def get_total_orders():
    query = text(
        """
            SELECT COUNT(*) AS total_orders
            FROM sales_data
            WHERE "Status" IN ('Shipped', 'Shipped - Delivered to Buyer')
                AND "Courier Status" = 'Shipped';
            """
    )
    return query_scalar(query, "total_orders")


@api.route("/api/data-by-category", methods=["GET"])
def get_data_by_category():
    query = text(
        """
            SELECT "Category",
                SUM("Amount") AS total_revenue,
                COUNT(*) AS total_orders
            FROM sales_data
            WHERE "Amount" IS NOT NULL
            GROUP BY "Category"
            ORDER BY total_revenue DESC;
            """
    )
    return query_table(query, "data_by_category")


@api.route("/api/sales-trend", methods=["GET"])
def get_sales_trend():
    query = text(
        """
        SELECT DATE_TRUNC('week', "Date"::timestamp) AS week,
            ROUND(SUM("Amount")::NUMERIC, 2) AS revenue
        FROM sales_data
        WHERE "Amount" IS NOT NULL
        GROUP BY week
        ORDER BY week;
    """
    )

    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            sales_trend = [
                {"x": row[0].strftime("%Y-%m-%d"), "y": row[1]}
                for row in result.fetchall()
            ]
    except Exception as e:
        print(f"Error fetching sales trend data: {e}")
        sales_trend = []

    return jsonify(sales_trend)


@api.route("/api/shipping-status-breakdown", methods=["GET"])
def get_shipping_status_breakdown():
    query = text(
        """
        SELECT "Courier Status" AS CourierStatus, COUNT(*) AS order_count
        FROM sales_data
        WHERE "Courier Status" IS NOT NULL
        GROUP BY "Courier Status"
        ORDER BY order_count DESC;
    """
    )
    return query_table(query, "shipping_status")


@api.route("/api/top-regions", methods=["GET"])
def get_top_regions():
    query = text(
        """
        SELECT "ship-state" AS Region, COUNT(*) AS order_count
        FROM sales_data
        WHERE "ship-state" IS NOT NULL
        GROUP BY "ship-state"
        ORDER BY order_count DESC
        LIMIT 10;
    """
    )
    return query_table(query, "top-regions")


def query_scalar(query, name):
    try:
        with engine.connect() as conn:
            result = conn.execute(query).scalar()
            result = result if result is not None else 0
    except Exception as e:
        print(f"Error querying {name}: {e}")
        result = 0
    return jsonify({name: result})


def query_table(query, name):
    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            data = [dict(row) for row in result.mappings()]
    except Exception as e:
        print(f"Error querying {name}: {e}")
        data = []
    return data

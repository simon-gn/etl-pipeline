from flask import Blueprint, jsonify
from flask import jsonify
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from scripts.database import get_session
from models.models import (
    Orders,
    OrderItems,
    Products,
    Shipping,
    States,
    PostalCodes,
)


api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def get_homepage():
    return "Welcome!"


@api.route("/api/sales", methods=["GET"])
def get_sales():
    try:
        with get_session() as session:
            results = (
                session.query(
                    Orders.order_id,
                    Orders.date,
                    Orders.status,
                    OrderItems.amount,
                    Products.category,
                    Shipping.courier_status,
                )
                .join(OrderItems, Orders.order_id == OrderItems.order_id)
                .join(Products, OrderItems.sku == Products.sku)
                .join(Shipping, Orders.order_id == Shipping.order_id)
                .filter(
                    OrderItems.amount.isnot(None), OrderItems.amount != float("nan")
                )
                .limit(100)
                .all()
            )
        return jsonify([dict(r) for r in results])

    except SQLAlchemyError as e:
        print(f"Error fetching sales data: {e}")
        return jsonify({"error": "An error occurred while fetching sales data"}), 500


@api.route("/api/total-revenue", methods=["GET"])
def get_total_revenue():
    try:
        with get_session() as session:
            total_revenue = (
                session.query(func.sum(OrderItems.amount))
                .join(Orders, Orders.order_id == OrderItems.order_id)
                .join(Shipping, Orders.order_id == Shipping.order_id)
                .filter(
                    Orders.status.in_(["Shipped", "Shipped - Delivered to Buyer"]),
                    Shipping.courier_status == "Shipped",
                    OrderItems.amount != float("nan"),
                )
                .scalar()
            )
        return jsonify({"total_revenue": total_revenue if total_revenue else 0})

    except SQLAlchemyError as e:
        print(f"Error fetching total revenue: {e}")
        return (
            jsonify({"error": "An error occurred while calculating total revenue"}),
            500,
        )


@api.route("/api/total-orders", methods=["GET"])
def get_total_orders():
    try:
        with get_session() as session:
            total_orders = (
                session.query(func.count(Orders.order_id))
                .join(Shipping, Orders.order_id == Shipping.order_id)
                .filter(
                    Orders.status.in_(["Shipped", "Shipped - Delivered to Buyer"]),
                    Shipping.courier_status == "Shipped",
                )
                .scalar()
            )
        return jsonify({"total_orders": total_orders})

    except SQLAlchemyError as e:
        print(f"Error fetching total orders: {e}")
        return (
            jsonify({"error": "An error occurred while calculating total orders"}),
            500,
        )


@api.route("/api/data-by-category", methods=["GET"])
def get_data_by_category():
    try:
        with get_session() as session:
            results = (
                session.query(
                    Products.category,
                    func.sum(OrderItems.amount).label("total_revenue"),
                    func.count(Orders.order_id).label("order_count"),
                )
                .join(OrderItems, Products.sku == OrderItems.sku)
                .join(Orders, Orders.order_id == OrderItems.order_id)
                .filter(
                    OrderItems.amount.isnot(None), OrderItems.amount != float("nan")
                )
                .group_by(Products.category)
                .order_by(func.sum(OrderItems.amount).desc())
                .all()
            )
            return jsonify(
                [
                    {
                        "category": row[0],
                        "total_revenue": float(row[1]),
                        "order_count": row[2],
                    }
                    for row in results
                ]
            )

    except SQLAlchemyError as e:
        print(f"Error fetching data by category: {e}")
        return (
            jsonify({"error": "An error occurred while fetching data by category"}),
            500,
        )


@api.route("/api/sales-trend", methods=["GET"])
def get_sales_trend():
    try:
        with get_session() as session:
            results = (
                session.query(
                    func.date_trunc("week", Orders.date).label("Week"),
                    func.coalesce(func.sum(OrderItems.amount), 0),
                )
                .join(Orders, Orders.order_id == OrderItems.order_id)
                .join(Shipping, Orders.order_id == Shipping.order_id)
                .filter(
                    OrderItems.amount.isnot(None),
                    OrderItems.amount != float("nan"),
                    Orders.status.in_(["Shipped", "Shipped - Delivered to Buyer"]),
                    Shipping.courier_status == "Shipped",
                )
                .group_by("Week")
                .order_by("Week")
                .all()
            )

        sales_trend = [
            {"x": row[0].strftime("%Y-%m-%d"), "y": row[1]} for row in results
        ]
        return jsonify(sales_trend)

    except SQLAlchemyError as e:
        print(f"Error fetching sales trend: {e}")
        return (
            jsonify({"error": "An error occurred while fetching sales trend data"}),
            500,
        )


@api.route("/api/shipping-status-breakdown", methods=["GET"])
def get_shipping_status_breakdown():
    try:
        with get_session() as session:
            results = (
                session.query(Shipping.courier_status, func.count(Shipping.order_id))
                .group_by(Shipping.courier_status)
                .order_by(func.count(Shipping.order_id).desc())
                .all()
            )

        shipping_status_breakdown = [
            {"courier_status": row[0], "order_count": row[1]} for row in results
        ]
        return jsonify(shipping_status_breakdown)

    except SQLAlchemyError as e:
        print(f"Error fetching shipping status breakdown: {e}")
        return (
            jsonify(
                {"error": "An error occurred while fetching shipping status breakdown"}
            ),
            500,
        )


@api.route("/api/top-regions", methods=["GET"])
def get_top_regions():
    try:
        with get_session() as session:
            results = (
                session.query(States.ship_state, func.count(Shipping.order_id))
                .join(PostalCodes, States.ship_state == PostalCodes.ship_state)
                .join(
                    Shipping, PostalCodes.ship_postal_code == Shipping.ship_postal_code
                )
                .group_by(States.ship_state)
                .order_by(func.count(Shipping.order_id).desc())
                .limit(10)
                .all()
            )

        top_regions = [{"region": row[0], "order_count": row[1]} for row in results]
        return jsonify(top_regions)

    except SQLAlchemyError as e:
        print(f"Error fetching top regions: {e}")
        return jsonify({"error": "An error occurred while fetching top regions"}), 500

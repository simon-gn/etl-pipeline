from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Date,
    Boolean,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Orders(Base):
    __tablename__ = "Orders"
    order_id = Column("Order ID", String, primary_key=True)
    date = Column("Date", Date)
    status = Column("Status", String)
    fulfilment = Column("Fulfilment", String)
    sales_channel = Column("Sales Channel", String)
    ship_service_level = Column("Ship Service Level", String)
    b2b = Column("B2B", Boolean)

    items = relationship("OrderItems", back_populates="order")
    shipping = relationship("Shipping", back_populates="order", uselist=False)


class Products(Base):
    __tablename__ = "Products"
    sku = Column("SKU", String, primary_key=True)
    style = Column("Style", String)
    category = Column("Category", String)
    size = Column("Size", String)
    asin = Column("ASIN", String)


class OrderItems(Base):
    __tablename__ = "OrderItems"
    order_id = Column("Order ID", String, ForeignKey(Orders.order_id), primary_key=True)
    sku = Column("SKU", String, ForeignKey(Products.sku), primary_key=True)
    qty = Column("Qty", Integer)
    currency = Column("Currency", String)
    amount = Column("Amount", Float)

    order = relationship("Orders", back_populates="items")
    product = relationship("Products")


class States(Base):
    __tablename__ = "States"
    ship_state = Column("Ship State", String, primary_key=True)
    ship_country = Column("Ship Country", String)


class PostalCodes(Base):
    __tablename__ = "PostalCodes"
    ship_postal_code = Column("Ship Postal Code", String, primary_key=True)
    ship_city = Column("Ship City", String)
    ship_state = Column(
        "Ship State", String, ForeignKey(States.ship_state), nullable=False
    )


class Shipping(Base):
    __tablename__ = "Shipping"
    order_id = Column("Order ID", String, ForeignKey(Orders.order_id), primary_key=True)
    ship_postal_code = Column(
        "Ship Postal Code",
        String,
        ForeignKey(PostalCodes.ship_postal_code),
        nullable=False,
    )
    courier_status = Column("Courier Status", String)

    order = relationship("Orders", back_populates="shipping")
    postal_code = relationship("PostalCodes")

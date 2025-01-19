import sys
import os
import pandas as pd
from scripts.database import get_session
from models.models import (
    Base,
    Orders,
    Products,
    OrderItems,
    Shipping,
    PostalCodes,
    States,
)
from etl.data_preprocessing import clean_data, normalize_data
from etl.data_transformation import map_dataframe_to_objects

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


def load_data():
    raw_data = pd.read_csv("../data/raw/Amazon Sale Report.csv")
    cleaned_data = clean_data(raw_data)

    (
        orders,
        products,
        order_items,
        shipping,
        postal_codes,
        states,
    ) = normalize_data(cleaned_data)

    orders.to_csv("../data/processed/orders.csv", index=False)
    products.to_csv("../data/processed/products.csv", index=False)
    order_items.to_csv("../data/processed/order_items.csv", index=False)
    shipping.to_csv("../data/processed/shipping.csv", index=False)
    postal_codes.to_csv("../data/processed/postal_codes.csv", index=False)
    states.to_csv("../data/processed/states.csv", index=False)

    # Map dataframes to SQLAlchemy objects
    orders = map_dataframe_to_objects(orders, Orders)
    products = map_dataframe_to_objects(products, Products)
    order_items = map_dataframe_to_objects(order_items, OrderItems)
    shipping = map_dataframe_to_objects(shipping, Shipping)
    postal_codes = map_dataframe_to_objects(postal_codes, PostalCodes)
    states = map_dataframe_to_objects(states, States)

    with get_session() as session:
        try:
            Base.metadata.drop_all(bind=session.bind)

            Base.metadata.create_all(bind=session.bind)

            session.add_all(states)
            session.commit()

            session.add_all(postal_codes)
            session.add_all(orders)
            session.add_all(products)
            session.commit()

            session.add_all(order_items)
            session.add_all(shipping)
            session.commit()

            print("Data uploaded successfully!")
        except Exception as e:
            session.rollback()
            print("An error occurred:", str(e))

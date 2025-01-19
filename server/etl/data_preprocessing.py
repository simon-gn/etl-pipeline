def clean_data(raw_data):
    # Drop unnecessary columns
    data = raw_data.drop(columns=["Unnamed: 22", "fulfilled-by", "promotion-ids"])

    # Strip leading/trailing whitespaces from column names
    data = data.rename(columns=lambda col: col.strip() if isinstance(col, str) else col)

    # Standardize column names
    column_mapping = {
        "Order ID": "order_id",
        "Date": "date",
        "Status": "status",
        "Fulfilment": "fulfilment",
        "Sales Channel": "sales_channel",
        "ship-service-level": "ship_service_level",
        "B2B": "b2b",
        "SKU": "sku",
        "Style": "style",
        "Category": "category",
        "Size": "size",
        "ASIN": "asin",
        "Qty": "qty",
        "currency": "currency",
        "Amount": "amount",
        "ship-postal-code": "ship_postal_code",
        "Courier Status": "courier_status",
        "ship-city": "ship_city",
        "ship-state": "ship_state",
        "ship-country": "ship_country",
    }
    data = data.rename(columns=column_mapping)

    # Standardize city and state names
    data["ship_city"] = data["ship_city"].str.title()
    data["ship_state"] = data["ship_state"].str.title()

    # data.loc[data["ship_postal_code"] == 411019.0, "ship_city"] = "Pune"

    return data


def normalize_data(data):
    orders = data[
        [
            "order_id",
            "date",
            "status",
            "fulfilment",
            "sales_channel",
            "ship_service_level",
            "b2b",
        ]
    ].drop_duplicates(subset=["order_id"])

    products = data[["sku", "style", "category", "size", "asin"]].drop_duplicates(
        subset=["sku"]
    )

    order_items = data[
        ["order_id", "sku", "qty", "currency", "amount"]
    ].drop_duplicates(subset=["order_id", "sku"])

    shipping = data[["order_id", "ship_postal_code", "courier_status"]].drop_duplicates(
        subset=["order_id"]
    )

    postal_codes = data[
        ["ship_postal_code", "ship_city", "ship_state"]
    ].drop_duplicates(subset=["ship_postal_code"])

    states = data[["ship_state", "ship_country"]].drop_duplicates(subset=["ship_state"])

    return (
        orders,
        products,
        order_items,
        shipping,
        postal_codes,
        states,
    )

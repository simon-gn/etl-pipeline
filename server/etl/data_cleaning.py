def clean_data(raw_data):
    data = raw_data.drop(columns=["Unnamed: 22", "fulfilled-by", "promotion-ids"])
    data.drop_duplicates(subset=["Order ID"], inplace=True)
    data["ship-city"] = data["ship-city"].str.title()
    data["ship-state"] = data["ship-state"].str.title()

    return data

def map_dataframe_to_objects(df, model_class):
    """
    Maps a DataFrame to SQLAlchemy model instances.

    Args:
        df (pd.DataFrame): The DataFrame to map.
        model_class: The SQLAlchemy model class.

    Returns:
        list: A list of model_class instances.
    """

    return [model_class(**row) for row in df.to_dict(orient="records")]

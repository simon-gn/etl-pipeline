def load_to_postgres(data, table_name, engine):
    data.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data loaded into table '{table_name}' successfully!")

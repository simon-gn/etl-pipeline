from app import create_app
from scripts.run_etl import load_data
import argparse

parser = argparse.ArgumentParser(description="ETL Pipeline")
parser.add_argument("--load", action="store_true", help="Load data into the database")
args = parser.parse_args()

app = create_app()

if __name__ == "__main__":
    if args.load:
        load_data()
        use_reloader = False
    else:
        use_reloader = True
        print("Skipping database load.")
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=use_reloader)

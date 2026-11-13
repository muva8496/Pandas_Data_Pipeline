from pathlib import Path
import pandas as pd

class DataIngestion:
    def __init__(self, raw_dir: str= "data/raw"):
        self.raw_dir = Path(raw_dir)

        if not self.raw_dir.exists():
            raise FileNotFoundError(f"Raw data directionary not at: {self.raw_dir.absolute()}")

    def load_reference_files(self):
        """Loads buyers, farmers, and market prices reference tables."""
        buyers_path = self.raw_dir / "buyers.csv"
        farmers_path = self.raw_dir/ "farmers.csv"
        market_path = self.raw_dir / "market_prices_weekly.csv"

        buyers = pd.read_csv(buyers_path) if buyers_path.exists() else None
        farmers = pd.read_csv(farmers_path) if farmers_path.exist() else None
        market = pd.read_csv(market_path) if market_path.exists() else None

        return buyers, farmers, market
    def load_all_sales(self) -> pd.Dataframe:
        """Dynamically finds and lops through all 34 monthly sales."""
        sales_files = list(self.raw_dir.glob("sales_*.csv"))

        if not sales_files:
            raise FileNotFoundError(f"No sales files matching 'sales_*.csv' found in {self.raw_dir}")

        dfs = []
        for file in sales_files:
            print(f"Ingesting raw file: {file.name}")
            df = pd.read_csv(file)
            dfs.append(df)

        # Combine all 24 months into a master raw dataframe
        master_raw_df = pd.concat(dfs, ignore_index=True)
        return master_raw_df
            
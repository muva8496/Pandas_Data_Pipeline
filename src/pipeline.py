from ingest  import DataIngestion
from clean import clean_sales_data
from transform import apply_business_transformations
from pathlib import Path

def run():
    print("=== PIPELIBE EXECUTION STARTED ===")

    # 1.Ingest
    ingester = DataIngestion("data/raw")
    raw_sales = ingester.load_all_sales()

    # 2.Clean
    cleaned_sales = clean_sales_data(raw_sales)

    # 3. Transform
    final_data = apply_business_transformations(cleaned_sales)


    # 4. Export to processed folder(ignored by git)
    output_path = Path("data/processed/master_processed_sales.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    final_data.to_csv(output_path, index=False)

    print(f"=== PIPELINE COMPLETE. Processed {len(final_data)} total rows. Saved to {output_path} ===")

if __name__ == "__main__":
    run()


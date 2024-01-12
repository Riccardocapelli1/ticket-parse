import os
from parser_def import parse_text_file

# Path to the 'text' folder in the current directory
folder_path = 'text'

# Create 'parquet' directory if it doesn't exist
output_folder = 'parquet'
os.makedirs(output_folder, exist_ok=True)

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        df_products, df_info = parse_text_file(file_path)
        if df_products is not None:
            # Save Product and Price Information
            product_output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_products.parquet")
            df_products.to_parquet(path=product_output_path, engine='auto', compression='snappy', index=None, partition_cols=None, storage_options=None)
            print(f"Product and Price Information saved to {product_output_path}")

            # Save Transaction Date and Total Amount Due
            info_output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_info.parquet")
            df_info.to_parquet(path=info_output_path, engine='auto', compression='snappy', index=None, partition_cols=None, storage_options=None)
            print(f"Transaction Date and Total Amount Due saved to {info_output_path}")

            print("\n")

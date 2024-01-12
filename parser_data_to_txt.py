import os
from parser_def import parse_text_file

# Path to the 'text' folder in the current directory
folder_path = 'text'

# List to store DataFrames for each file
dataframes = []

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        df_products, df_info = parse_text_file(file_path)
        if df_products is not None:
            # Add more processing or saving steps if needed
            print("Product and Price Information:")
            print(df_products)
            print("\nTransaction Date and Total Amount Due:")
            print(df_info)
            print("\n")
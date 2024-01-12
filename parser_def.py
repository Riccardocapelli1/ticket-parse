import pandas as pd
import re

def parse_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Check if the file contains 'lidl' or 'LIDL' in the first five lines
    if any('lidl' in line.lower() for line in lines[:5]):
        products = []
        parsing_products = False
        transaction_date = None
        total_amount_due = None

        # Loop to extract product and price information
        for line in lines:
            # Start parsing from the line containing 'EUR' or 'eur'
            if 'eur' in line.lower():
                parsing_products = True

            # Stop parsing at the line containing 'Total' or 'total'
            if 'total' in line.lower():
                break

            if parsing_products:
                # Exclude lines containing 'EUR/kg'
                if 'eur/kg' in line.lower():
                    continue

                # Extract product name and price using a modified regular expression
                match = re.search(r'([\w\s.]+)\s+([\d.,]+)\s?([BEFbebf])', line)
                if match:
                    product_name = match.group(1).strip()
                    price = match.group(2).replace(',', '.').strip() + match.group(3).upper()

                    # Remove the last letter from the price column
                    price = price[:-1] if price.endswith(('B', 'E', 'F', '8B', '8E', '8F')) else price

                    # Filter out product names that are just numbers
                    if not product_name.isdigit():
                        products.append({'product_name': product_name, 'price': price})

        # Loop to extract transaction date and total amount due information
        for i, line in enumerate(lines):
            # Check for the line containing 'VENDITA'
            if 'vendita' in line.lower():
                # Extract the date and total amount due from two lines below 'VENDITA'
                transaction_date_line = lines[i + 2].strip()
                total_amount_due_line = lines[i + 3].strip()

                # Extract the date and total amount due using a regular expression
                date_match = re.search(r'(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2})', transaction_date_line)
                amount_match = re.search(r'IMP.:\s+([\d.,]+)\s+([BEFbebf])', total_amount_due_line)

                if date_match:
                    transaction_date = date_match.group(1)

                if amount_match:
                    total_amount_due = amount_match.group(1) + amount_match.group(2)
                    total_amount_due = total_amount_due[:-1].replace(',', '.') if total_amount_due.endswith(('C', 'E', 'N', 'Z')) else total_amount_due.replace(',', '.')

        # Create a Pandas DataFrame for product and price information
        df_products = pd.DataFrame(products)

        # Create a DataFrame for transaction date and total amount due
        df_info = pd.DataFrame({'transaction_date': [transaction_date], 'total_amount_due': [total_amount_due]})

        return df_products, df_info
    else:
        return None, None


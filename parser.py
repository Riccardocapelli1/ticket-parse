import pandas as pd

def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the starting index of relevant lines
    start_index = next((i for i, line in enumerate(lines) if 'lidl' in line.lower()), None)

    if start_index is None:
        print("Lidl not found in the first 5 lines.")
        return None

    # Find the ending index of relevant lines
    end_index = next((i for i, line in enumerate(lines) if 'total' in line.lower()), None)

    if end_index is None:
        print("Total not found.")
        return None

    # Extract the relevant lines
    relevant_lines = lines[start_index:end_index]

    # Parse the lines to extract product name and price
    data = []
    for line in relevant_lines:
        if 'eur' in line.lower() or 'total' in line.lower():
            continue  # Skip lines containing 'eur' or 'total'

        parts = line.split()
        if len(parts) >= 4:
            product_name = ' '.join(parts[:-3])
            price_str = parts[-2].replace(',', '.')
            try:
                price = float(price_str)
                data.append((product_name, price))
            except ValueError:
                print(f"Error parsing price in line: {line}")

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Product Name', 'Price'])

    return df

# Replace 'file_path.txt' with the actual path to your file
file_path = './text/1-lidl-text.txt'
result_df = parse_file(file_path)

if result_df is not None:
    # Display the resulting DataFrame
    print(result_df)


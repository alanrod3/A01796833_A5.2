import json
import sys
import time
import os


def load_json_file(filename):
    """
    Loads a JSON file and handles invalid file errors.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None


def create_price_map(price_list):
    """
    Converts the price list into a dictionary for O(1) access time.
    """
    price_map = {}
    for item in price_list:
        key = item.get('title') or item.get('product') or item.get('Product')
        price = item.get('price') or item.get('Price')

        if key and price is not None:
            price_map[key] = price
    return price_map


def compute_total_cost(price_map, sales_list):
    """
    Computes total sales cost.
    """
    total_cost = 0.0

    for sale in sales_list:
        product_name = (
            sale.get('Product') or sale.get('product') or sale.get('title')
        )
        quantity = sale.get('Quantity') or sale.get('quantity')

        if not product_name or quantity is None:
            print(f"Error: Invalid sale record: {sale}")
            continue

        if product_name in price_map:
            try:
                cost = price_map[product_name] * quantity
                total_cost += cost
            except TypeError:
                print(f"Error: Invalid data for '{product_name}'")
        else:
            print(f"Error: '{product_name}' not found in catalogue.")

    return total_cost


def main():
    """
    Main function to execute the program logic.
    """
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    price_data = load_json_file(price_file)
    sales_data = load_json_file(sales_file)

    if price_data is None or sales_data is None:
        sys.exit(1)

    price_map = create_price_map(price_data)
    total_cost = compute_total_cost(price_map, sales_data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Output formatting
    output_lines = [
        "TOTAL SALES COST REPORT",
        "-" * 30,
        f"Total Cost: ${total_cost:,.2f}",
        f"Execution Time: {elapsed_time:.4f} seconds"
    ]
    output_string = "\n".join(output_lines)

    # Print to Console
    print("\n" + output_string)

    # --- PATH HANDLING FOR OUTPUT ---
    # This logic finds the 'results' folder automatically
    # It assumes 'results' is at the same level as the 'source' folder
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(current_script_dir, '..', 'results')

    # If results folder doesn't exist (e.g. folder structure changed),
    # fallback to current working directory
    if not os.path.exists(results_dir):
        try:
            os.makedirs(results_dir)
        except OSError:
            results_dir = os.getcwd()

    output_path = os.path.join(results_dir, "SalesResults.txt")

    # Write to File
    try:
        with open(output_path, "w", encoding='utf-8') as result_file:
            result_file.write(output_string)
        print(f"\nResults saved to: {output_path}")
    except Exception as e:
        print(f"Error writing to results file: {e}")


if __name__ == "__main__":
    main()
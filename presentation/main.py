"""
main.py
Entry point for the milk radiation analysis program.
Author: Jiaxiang Yuan
"""

from persistence.dataset_handler import load_milk_dataset, get_raw_data
from business.statistics_calculator import calculate_average_radiation
from chart.pie_chart import generate_pie_chart

DATASET_PATH = "data/milk_dataset.csv"

def display_menu():
    print("\n=== Milk Radiation Analysis Menu ===")
    print("1. Load dataset")
    print("2. View average Sr-90 by province")
    print("3. Show Pie Chart")
    print("4. Exit")

def load_data():
    print("[INFO] Loading dataset...")
    records = load_milk_dataset(DATASET_PATH)
    if records:
        print(f"[SUCCESS] Loaded {len(records)} records.")
    else:
        print("[WARNING] No records loaded.")

def show_average_radiation():
    print("[INFO] Calculating average radiation by province...")
    records = load_milk_dataset(DATASET_PATH)
    if not records:
        print("[ERROR] No data loaded. Please load the dataset first.")
        return

    averages = calculate_average_radiation(records)
    for province, avg in averages.items():
        print(f"{province}: {avg:.4f} Bq/L")

def show_pie_chart():
    print("[INFO] Generating pie chart of radiation by province...")
    data = get_raw_data()
    generate_pie_chart(data)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            load_data()
        elif choice == '2':
            show_average_radiation()
        elif choice == '3':
            show_pie_chart()
        elif choice == '4':
            print("[EXIT] Goodbye!")
            break
        else:
            print("[WARNING] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

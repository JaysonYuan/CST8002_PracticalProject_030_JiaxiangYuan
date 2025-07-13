import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB
from persistence.dataset_handler import load_milk_dataset

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATASET_PATH = os.path.join(PROJECT_ROOT, "dataset", "nms_strontium90_milk_ssn_strontium90_lait.csv")

def display_menu():
    print("\n--- Milk Radiation Record Viewer ---")
    print("Author: Jiaxiang Yuan")
    print("Select a display format:")
    print("1. Dash-separated format")
    print("2. Label-style format")
    print("3. Exit")

def main():
    all_records = load_milk_dataset(DATASET_PATH)
    print(f"[DEBUG] Loaded {len(all_records)} records.")  # Debug info

    if not all_records:
        print("[ERROR] No records loaded. Please check the dataset file.")
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\n--- Dash-separated Records ---")
            for record in all_records:
                print(FormattedRecordA(record.id, record.name, record.value).display())

        elif choice == '2':
            print("\n--- Label-style Records ---")
            for record in all_records:
                print(FormattedRecordB(record.id, record.name, record.value).display())

        elif choice == '3':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

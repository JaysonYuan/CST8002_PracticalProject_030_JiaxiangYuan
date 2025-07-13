"""
main.py
CLI to demonstrate polymorphism using milk Sr90 dataset records.

Author: Jiaxiang Yuan
"""

from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB
from persistence.dataset_handler import load_milk_dataset

DATASET_PATH = "./dataset/nms_strontium90_milk_ssn_strontium90_lait.csv"

def display_menu():
    print("\n--- Milk Radiation Record Viewer ---")
    print("Author: Jiaxiang Yuan")
    print("Select a display format:")
    print("1. Dash-separated format")
    print("2. Label-style format")
    print("3. Exit")

def main():
    all_records = load_milk_dataset(DATASET_PATH)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- Dash-separated Records ---")
            for record in all_records:
                if isinstance(record, FormattedRecordA):
                    print(record.display())

        elif choice == '2':
            print("\n--- Label-style Records ---")
            for record in all_records:
                if isinstance(record, FormattedRecordB):
                    print(record.display())

        elif choice == '3':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

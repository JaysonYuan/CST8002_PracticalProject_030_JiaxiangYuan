"""
presentation/main.py
Console UI for Sr-90 Milk Records System.

Program by Jiaxiang Yuan
"""

import os
import sys

# Adjust import paths if needed (if you run from project root)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from persistence.file_handler import load_records_from_csv, save_records_to_csv, generate_uuid_filename
from business.record_manager import RecordManager
from model.record import Record

DATASET_FILE = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'nms_strontium90_milk_ssn_strontium90_lait.csv')
PROGRAMMER_NAME = "Program by Jiaxiang Yuan"

def print_header():
    print("=" * 40)
    print(f"=== Sr-90 Milk Records System ===")
    print(PROGRAMMER_NAME)
    print("=" * 40)

def print_menu():
    print("\nMenu Options:")
    print("1. Reload data from CSV")
    print("2. Display all records")
    print("3. Search records by province")
    print("4. Save records to new CSV file")
    print("5. Add a new record")
    print("6. Edit a record")
    print("7. Delete a record")
    print("8. Exit")

def display_records(records):
    if not records:
        print("No records to display.")
        return
    for i, r in enumerate(records):
        print(f"{i}: {r}")
        if (i + 1) % 10 == 0:
            print(PROGRAMMER_NAME)

def input_record_data():
    """
    Prompt user for record fields and return a Record object.
    """
    print("Enter new record details:")
    sample_type = input("Sample Type: ").strip()
    type_ = input("Type: ").strip()
    start_date = input("Start Date: ").strip()
    stop_date = input("Stop Date: ").strip()
    station_name = input("Station Name: ").strip()
    province = input("Province: ").strip()
    sr90_activity = input("Sr90 Activity (Bq/L): ").strip()
    sr90_error = input("Sr90 Error (Bq/L): ").strip()
    sr90_calcium_activity = input("Sr90 Calcium Activity (Bq/g): ").strip()

    return Record(sample_type, type_, start_date, stop_date,
                  station_name, province, sr90_activity,
                  sr90_error, sr90_calcium_activity)

def main():
    record_manager = RecordManager()
    # Load data at startup
    print_header()
    print(f"Loading dataset from: {DATASET_FILE}")
    records = load_records_from_csv(DATASET_FILE)
    record_manager.load_records(records)
    print(f"Loaded {len(records)} records.\n")

    while True:
        print_header()
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()
        print(PROGRAMMER_NAME)

        if choice == '1':
            # Reload data from CSV
            records = load_records_from_csv(DATASET_FILE)
            record_manager.load_records(records)
            print(f"Reloaded {len(records)} records from dataset.")

        elif choice == '2':
            # Display all records
            all_records = record_manager.get_all_records()
            display_records(all_records)

        elif choice == '3':
            # Search by province
            prov = input("Enter province to search: ").strip()
            found = record_manager.find_records_by_province(prov)
            print(f"Found {len(found)} record(s) for province '{prov}':")
            display_records(found)

        elif choice == '4':
            # Save records to new CSV file
            filename = generate_uuid_filename()
            save_path = os.path.join(os.path.dirname(__file__), '..', filename)
            save_records_to_csv(save_path, record_manager.get_all_records())

        elif choice == '5':
            # Add a new record
            new_rec = input_record_data()
            record_manager.add_record(new_rec)
            print("Record added.")

        elif choice == '6':
            # Edit a record
            idx_str = input("Enter index of record to edit: ").strip()
            if idx_str.isdigit():
                idx = int(idx_str)
                if 0 <= idx < len(record_manager.get_all_records()):
                    print("Enter new values for record:")
                    new_rec = input_record_data()
                    record_manager.edit_record(idx, new_rec)
                    print("Record updated.")
                else:
                    print("Index out of range.")
            else:
                print("Invalid index.")

        elif choice == '7':
            # Delete a record
            idx_str = input("Enter index of record to delete: ").strip()
            if idx_str.isdigit():
                idx = int(idx_str)
                if record_manager.delete_record(idx):
                    print("Record deleted.")
                else:
                    print("Index out of range.")
            else:
                print("Invalid index.")

        elif choice == '8':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1-8.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

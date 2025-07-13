"""
main.py
CLI to demonstrate polymorphism using milk Sr90 dataset records.
Implements CRUD operations and dynamic formatting.

Author: Jiaxiang Yuan
"""

import sys
import os

# Add project root to path for importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB
from persistence.dataset_handler import load_milk_dataset

# Define path to dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATASET_PATH = os.path.join(PROJECT_ROOT, "dataset", "nms_strontium90_milk_ssn_strontium90_lait.csv")

# In-memory list of all records
all_records = []
next_id = 0  # Track next available ID for new records


def display_menu():
    """
    Displays the main CLI menu.
    """
    print("\n--- Milk Radiation Record Viewer ---")
    print("Author: Jiaxiang Yuan")
    print("Select an option:")
    print("1. Display records (dash-separated)")
    print("2. Display records (label-style)")
    print("3. Add a new record")
    print("4. Edit a record")
    print("5. Delete a record")
    print("6. Reload dataset")
    print("7. Exit")


def display_records(format_type='dash'):
    """
    Displays all records in the selected format.

    :param format_type: 'dash' for FormattedRecordA, 'label' for FormattedRecordB
    """
    if not all_records:
        print("[INFO] No records to display.")
        return

    print("\n--- Milk Radiation Records ---")
    for idx, record in enumerate(all_records):
        prefix = f"{idx}: "
        if format_type == 'dash':
            print(prefix + FormattedRecordA(record.id, record.name, record.value).display())
        else:
            print(prefix + FormattedRecordB(record.id, record.name, record.value).display())


def generate_next_id():
    """
    Generates the next unique ID in padded 3-digit format.

    :return: String ID like '005'
    """
    global next_id
    new_id = f"{next_id:03d}"
    next_id += 1
    return new_id


def add_record():
    """
    Prompts user to input a new record and adds it to the list.
    """
    station = input("Enter station name: ").strip()
    province = input("Enter province code: ").strip()
    start_date = input("Enter start date (e.g. 01-Jan-90): ").strip()

    try:
        sr90 = float(input("Enter Sr90 activity (Bq/L): ").strip())
    except ValueError:
        print("[ERROR] Invalid numeric value.")
        return

    record_id = generate_next_id()
    name = f"{station}-{province}-{start_date}"
    record = FormattedRecordA(record_id, name, sr90)  # Default to Format A
    all_records.append(record)
    print(f"[INFO] Record {record_id} added.")


def find_record_by_id(record_id):
    """
    Finds a record by ID.

    :param record_id: ID to search
    :return: (index, record) tuple or (None, None)
    """
    for idx, rec in enumerate(all_records):
        if rec.id == record_id:
            return idx, rec
    return None, None


def edit_record():
    """
    Edits an existing record by ID.
    """
    record_id = input("Enter record ID to edit: ").strip()
    idx, record = find_record_by_id(record_id)

    if record is None:
        print("[ERROR] Record not found.")
        return

    print(f"Editing record {record_id}:")
    try:
        station, province, start_date = record.name.split('-', 2)
    except ValueError:
        print("[WARN] Unexpected name format. Defaulting to empty values.")
        station = province = start_date = ""

    print(f"Current station: {station}")
    new_station = input("New station (leave blank to keep): ").strip()
    print(f"Current province: {province}")
    new_province = input("New province (leave blank to keep): ").strip()
    print(f"Current start date: {start_date}")
    new_start_date = input("New start date (leave blank to keep): ").strip()
    print(f"Current Sr90 activity: {record.value}")
    new_value_str = input("New Sr90 activity (leave blank to keep): ").strip()

    # Keep old values if user input is blank
    station = new_station if new_station else station
    province = new_province if new_province else province
    start_date = new_start_date if new_start_date else start_date
    value = record.value

    if new_value_str:
        try:
            value = float(new_value_str)
        except ValueError:
            print("[ERROR] Invalid number. Keeping original value.")

    new_name = f"{station}-{province}-{start_date}"

    # Keep same record type (A or B)
    if isinstance(record, FormattedRecordA):
        new_record = FormattedRecordA(record.id, new_name, value)
    else:
        new_record = FormattedRecordB(record.id, new_name, value)

    all_records[idx] = new_record
    print(f"[INFO] Record {record_id} updated.")


def delete_record():
    """
    Deletes a record by ID with confirmation.
    """
    record_id = input("Enter record ID to delete: ").strip()
    idx, record = find_record_by_id(record_id)

    if record is None:
        print("[ERROR] Record not found.")
        return

    confirm = input(f"Are you sure you want to delete record {record_id}? (y/n): ").strip().lower()
    if confirm == 'y':
        all_records.pop(idx)
        print(f"[INFO] Record {record_id} deleted.")
    else:
        print("[INFO] Deletion cancelled.")


def reload_data():
    """
    Reloads the dataset from CSV and updates in-memory list.
    """
    global all_records, next_id
    all_records = load_milk_dataset(DATASET_PATH)

    # Update next_id to avoid duplication
    if all_records:
        max_id_num = max(int(r.id) for r in all_records if r.id.isdigit())
        next_id = max_id_num + 1
    else:
        next_id = 0

    print(f"[INFO] Reloaded {len(all_records)} records.")


def main():
    """
    Entry point: starts CLI loop and handles user interaction.
    """
    reload_data()
    print(f"[DEBUG] Loaded {len(all_records)} records.")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_records('dash')
        elif choice == '2':
            display_records('label')
        elif choice == '3':
            add_record()
        elif choice == '4':
            edit_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            reload_data()
        elif choice == '7':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select again.")


if __name__ == "__main__":
    main()

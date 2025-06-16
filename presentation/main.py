"""
presentation/main.py
Command-line interface for interacting with the Sr-90 record system.

Program by Jiaxiang Yuan
"""

from business.record_manager import RecordManager
from persistence.file_handler import load_records_from_csv, save_records_to_csv, generate_uuid_filename

def display_menu():
    print("\n=== Sr-90 Milk Records System ===")
    print("Program by Jiaxiang Yuan")
    print("1. Load records from CSV")
    print("2. Display all records")
    print("3. Search by province")
    print("4. Save records to new CSV")
    print("5. Add a new record")
    print("6. Exit")


def main():
    manager = RecordManager()
    file_path = "dataset/nms_strontium90_milk_ssn_strontium90_lait.csv"

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.records = load_records_from_csv(file_path)
            print(f"Loaded {len(manager.records)} records.")
        elif choice == "2":
            for i, r in enumerate(manager.get_all_records()):
                print(f"[{i}] {r}")
                if (i + 1) % 10 == 0:
                    print("Program by Jiaxiang Yuan")
        elif choice == "3":
            prov = input("Enter province abbreviation (e.g., ON): ")
            results = manager.search_by_province(prov)
            print(f"Found {len(results)} records in {prov.upper()}:")
            for r in results:
                print(r)
        elif choice == "4":
            save_path = generate_uuid_filename()
            save_records_to_csv(save_path, manager.get_all_records())
            print(f"Records saved to {save_path}")
        elif choice == "5":
            sample_type = input("Sample Type: ")
            type_ = input("Type: ")
            start_date = input("Start Date: ")
            stop_date = input("Stop Date: ")
            station_name = input("Station Name: ")
            province = input("Province: ")
            sr90_activity = input("Sr90 Activity: ")
            sr90_error = input("Sr90 Error: ")
            sr90_calcium_activity = input("Sr90 Calcium Activity: ")

            from model.record import Record
            new_record = Record(
                sample_type, type_, start_date, stop_date,
                station_name, province, sr90_activity,
                sr90_error, sr90_calcium_activity
            )
            manager.add_record(new_record)
            print("New record added.")
        elif choice == "6":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

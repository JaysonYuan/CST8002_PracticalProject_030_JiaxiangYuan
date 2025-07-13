from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB

def display_menu():
    print("Program by Jayson YUAN")
    print("Choose a display format:")
    print("1. Dash-separated")
    print("2. Label format")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            records = [
                FormattedRecordA(1, "milk", 3.99),
                FormattedRecordA(2, "cheese", 5.50)
            ]
        elif choice == '2':
            records = [
                FormattedRecordB(1, "milk", 3.99),
                FormattedRecordB(2, "cheese", 5.50)
            ]
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input")
            continue

        for rec in records:
            print(rec.display())

if __name__ == "__main__":
    main()

"""
main.py
Milk Radiation Record Viewer CLI

Author: Jiaxiang Yuan
"""

from persistence import dataset_handler

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
    print("7. Show Pie Chart") 
    print("8. Exit")

def main():
    """
    Main control loop for CLI program.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Displaying records (dash-separated)...")
        elif choice == '2':
            print("Displaying records (label-style)...")
        elif choice == '3':
            print("Adding new record...")
        elif choice == '4':
            print("Editing record...")
        elif choice == '5':
            print("Deleting record...")
        elif choice == '6':
            print("Reloading dataset...")
        elif choice == '7':
            print("Pie chart option selected.")  
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

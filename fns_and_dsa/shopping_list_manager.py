def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")

        if choice == '1':  # Add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to the shopping list.\n")

        elif choice == '2':  # Remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"'{item}' has been removed from the shopping list.\n")
            else:
                print(f"'{item}' was not found in the shopping list.\n")

        elif choice == '3':  # View the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                print("")  # Add a new line for spacing
            else:
                print("Your shopping list is currently empty.\n")

        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")  # Handle invalid choices

if __name__ == "__main__":
    main()

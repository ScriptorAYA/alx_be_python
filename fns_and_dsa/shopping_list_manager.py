def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} added to the list.")

        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print("Item not found in the list.")

        elif choice == 3:
            if len(shopping_list) == 0:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
                for item in shopping_list:
                    print(item)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


def add_items(tup):
    item = input("Enter item: ")
    return tup + (item,)

def show_length(tup):
    print(f"Length of the tuple: {len(tup)}")

def check_item(tup):
    item = input("Enter the item to check: ")
    print(f"Is '{item}' present in the tuple? {'Yes' if item in tup else 'No'}")

def get_item(tup):
    try:
        index = int(input("Enter the index to access: "))
        print(f"Item at index {index}: {tup[index]}")
    except IndexError:
        print("Index out of range")
    except ValueError:
        print("Invalid index")

t = ()

while True:
    print("\nMenu:")
    print("1. Add item to the tuple")
    print("2. Show length of the tuple")
    print("3. Check for an item in the tuple")
    print("4. Get an item from the tuple")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        t = add_items(t)
        print(f"Tuple after adding item: {t}")
    elif choice == '2':
        show_length(t)
    elif choice == '3':
        check_item(t)
    elif choice == '4':
        get_item(t)
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again")

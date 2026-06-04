
def add_user(users):
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            break
        else:
            print("Name cannot be empty.")

    if users:
        new_id = max(user["id"] for user in users) + 1
    else:
        new_id = 1


    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Age must be an integer.")

    user = {
        "id": new_id,
        "name": name,
        "age": age,
    }

    users.append(user)
    print("User added successfully.")

def list_users(users):
    if not users:
        print("User not exist.")
        return

    for user in users:
        print(f'ID: {user["id"]}, Name: {user["name"]}, Age: {user["age"]}')


def delete_user(users):
    if not users:
        print("User not exist.")
        return

    while True:
        try:
            user_id = int(input("Please enter user id:"))
            break
        except ValueError:
            print("User ID must be an integer.")

    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            print("User deleted successfully. ")
            return

    print("User ID not found.")

def print_menu():
    print("""
    --- User Management ---
    1. Add new user
    2. List users
    3. Delete user
    4. Exit
    """)

def main():
    users = []

    while True:
        print_menu()

        choice = input("Please enter your option:")

        if choice == '1':
            add_user(users)

        elif choice == '2':
            list_users(users)

        elif choice == '3':
            delete_user(users)

        elif choice == '4':
            break

        else:
            print("\nInvalid choice.")

if __name__ == '__main__':
    main()


from storage import load_users
from services import add_user, list_users, delete_user


def print_menu():
    print("""
    --- User Management ---
    1. Add new user
    2. List users
    3. Delete user
    4. Exit
    """)


def main():
    users = load_users()

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


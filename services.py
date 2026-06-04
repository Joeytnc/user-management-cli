from storage import save_users

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
    save_users(users)
    print("User added successfully.")


def list_users(users):
    if not users:
        print("No users in system.")
        return

    for user in users:
        print(f'ID: {user["id"]}, Name: {user["name"]}, Age: {user["age"]}')


def delete_user(users):
    if not users:
        print("No users in system.")
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
            save_users(users)
            print("User deleted successfully. ")
            return
    print("User ID not found.")

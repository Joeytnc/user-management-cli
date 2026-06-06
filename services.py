from storage import save_users

def create_user(users, name, age):
    if users:
        new_id = max(user["id"] for user in users) + 1
    else:
        new_id = 1

    user = {
            "id": new_id,
            "name": name,
            "age": age,
        }

    users.append(user)
    save_users(users)
    return user


def add_user(users):
    name = input("Please enter your name: ").strip()
    age = int(input("Please enter your age: "))
    return create_user(users, name, age)


def list_users(users):
    if not users:
        print("No users in system.")
        return

    for user in users:
        print(f'ID: {user["id"]}, Name: {user["name"]}, Age: {user["age"]}')


def get_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def update_user_by_id(users, user_id, name, age):
    for user in users:
        if user["id"] == user_id:
            user["name"] = name
            user["age"] = age

            save_users(users)
            return user
    return None


def delete_user(users):

    user_id = int(input("Please enter user id:"))
    success = delete_user_by_id(users, user_id)
    if success:
        print("User deleted successfully.")
    else:
        print("User ID not found.")


def delete_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            save_users(users)
            return True

    return False

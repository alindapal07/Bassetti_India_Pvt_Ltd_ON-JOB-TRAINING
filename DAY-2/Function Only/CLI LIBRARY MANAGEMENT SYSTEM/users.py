users = [
    {
        "id": 1,
        "name": "Pritam"
    }
]

def register_user(user_id, name):
    for user in users:
        if user["id"] == user_id:
            raise ValueError("User ID already exists")

    users.append({
        "id": user_id,
        "name": name
    })

    return "User registered successfully"

def user_exists(user_id):
    for user in users:
        if user["id"] == user_id:
            return True

    return False
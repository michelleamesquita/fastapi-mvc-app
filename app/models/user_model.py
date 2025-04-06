# app/models/user_model.py

fake_users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

def get_all_users():
    return fake_users_db

def get_user_by_id(user_id: int):
    return next((user for user in fake_users_db if user["id"] == user_id), None)

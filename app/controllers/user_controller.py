# app/controllers/user_controller.py

from app.models.user_model import get_all_users, get_user_by_id

def fetch_users():
    return get_all_users()

def fetch_user(user_id: int):
    return get_user_by_id(user_id)

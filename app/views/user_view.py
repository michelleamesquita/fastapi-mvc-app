# app/views/user_view.py

from fastapi import APIRouter, HTTPException
from app.controllers.user_controller import fetch_users, fetch_user

router = APIRouter()

@router.get("/users")
def get_users():
    return fetch_users()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = fetch_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

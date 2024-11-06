from fastapi import FastAPI, Path
from typing import Annotated

main_app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}


@main_app.get('/users')
async def get_users() -> dict:
    return users_db


@main_app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Rinat")],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example="42")]) -> str:
    user_id = str(int(max(users_db, key=int)) + 1)
    users_db[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@main_app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: Annotated[
    str, Path(min_length=5, max_length=20, description="Enter username", example="Rinat")],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example="42")]) -> str:
    users_db[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} has ben updated"


@main_app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users_db.pop(user_id)
    return f"The user {user_id} has ben deleted"

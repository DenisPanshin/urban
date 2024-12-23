from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def main() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, title='Enter username')],
                   age: Annotated[int, Path(ge=18, le=120, title='Enter age')]) -> str:
    max_value = str(int(max(users)) + 1)
    users[max_value] = f'Имя: {username}, возраст: {age}'
    return f'User {max_value} is registered'


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=0, le=100, title='Enter id')],
                      username: Annotated[str, Path(min_length=5, max_length=20, title='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, title='Enter age')]) -> str:
    if str(user_id) in users:
        users[str(user_id)] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} is updated'
    raise HTTPException(status_code=404, detail="User id не найден")


@app.delete("/user/{user_id}")
async def del_user(user_id: Annotated[int, Path(ge=0, le=100, title='Enter id')]) -> str:
    if str(user_id) in users:
        users.pop(str(user_id))
        return f'User {user_id} has been deleted'
    raise HTTPException(status_code=404, detail="User id не найден")

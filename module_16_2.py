from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/user/{username}/{age}")
async def getuserinfo(username: Annotated[str, Path(min_length=5, max_length=20, title='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, title='Enter age')]) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get("/user/admin")
async def getadmin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def getid(user_id: Annotated[int, Path(ge=1, le=100, title='Enter User ID')]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get("/")
async def main() -> dict:
    return {'message': 'Главная страница'}

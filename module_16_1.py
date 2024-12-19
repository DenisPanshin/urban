from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{username}/{age}")
async def getuserinfo(username: str, age: str) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get("/user/admin")
async def getadmin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def getid(user_id) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get("/")
async def main() -> dict:
    return {'message': 'Главная страница'}

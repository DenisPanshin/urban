from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{username}/{age}")
async def getuserinfo(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


@app.get("/user/admin")
async def getadmin() -> str:
    return f'Вы вошли как администратор'


@app.get("/user/{user_id}")
async def getid(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get("/")
async def main() -> str:
    return f'Главная страница'

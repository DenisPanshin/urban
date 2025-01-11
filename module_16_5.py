from fastapi import FastAPI, Path, HTTPException, Request
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory='templates')
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def get(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def main(request: Request, user_id: Annotated[int, Path(ge=1)]) -> HTMLResponse:
    for user in users:
        if int(user['id']) == int(user_id):
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, title='Enter username')],
                   age: Annotated[int, Path(ge=18, le=120, title='Enter age')]) -> dict:
    max_value = 0
    if users:
        max_value = users[-1]['id'] + 1
    else:
        max_value += 1
    users.append({'id': max_value, 'username': username, 'age': age})
    return users[-1]


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=0, le=100, title='Enter id')],
                      username: Annotated[str, Path(min_length=5, max_length=20, title='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, title='Enter age')]) -> dict:
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            users[i] = {'id': user_id, 'username': username, 'age': age}
            return users[i]
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def del_user(user_id: Annotated[int, Path(ge=0, le=100, title='Enter id')]) -> dict:
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            return users.pop(i)
    else:
        raise HTTPException(status_code=404, detail="User was not found")

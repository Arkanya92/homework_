from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    age: int

app = FastAPI()

templates = Jinja2Templates(directory='templates')

users: List[User] = []

@app.get('/', response_class=HTMLResponse)
async def get_main(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get('/users/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse('users.html', {'request': request, 'user': user})
    raise HTTPException(status_code=404, detail='User not found')

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5,
                                      max_length=20,
                                      title='username',
                                      description='Enter username',
                                      example='Maxim')],
        age: Annotated[int, Path(gt=0,
                                 ge=18,
                                 le=120,
                                 title='age',
                                 description='Enter age',
                                 example='25')]
):
    user_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(title='user_id',
                                     description='Enter user ID',
                                     example='1')],
        username: Annotated[str, Path(min_length=5,
                                      max_length=20,
                                      title='username',
                                      description='Enter username',
                                      example='Maxim')],
        age: Annotated[int, Path(gt=0,
                                 ge=18,
                                 le=120,
                                 title='age',
                                 description='Enter age',
                                 example='25')]
):
    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return u
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(title='user_id',
                                     description='Enter user ID',
                                     example='1')]
):
    for i, u in enumerate(users):
        if u.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail='User was not found')
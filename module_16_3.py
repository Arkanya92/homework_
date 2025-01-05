from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
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
) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = {'Имя': username, 'возраст': age}
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, Path(title='user_id',
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
) -> str:
    users[user_id] = {'Имя': username, 'возраст': age}
    return f'The user {user_id} is update'

@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[str, Path(title='user_id',
                                     example='1')]
) -> str:
    users.pop(user_id)
    return f'User {user_id} has been delete'
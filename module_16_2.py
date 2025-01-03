from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def home_page() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def page_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def page_user(user_id: Annotated[int, Path(gt=0,
                                                 ge=1,
                                                 le=100,
                                                 title='User ID',
                                                 description='Enter User ID',
                                                 example='1')]):
    return {'message': f'Вы воошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def info_user(
        username: Annotated[str, Path(min_length=5,
                                      max_length=20,
                                      title='username',
                                      description='Enter username',
                                      example='UrbanUser')],
        age: Annotated[int, Path(gt=0,
                                 ge=18,
                                 le=120,
                                 title='age',
                                 description='Enter age',
                                 example='25')]
):
    return {'message': f'Информация о ползователе. Имя: {username}, Возраст: {age}'}
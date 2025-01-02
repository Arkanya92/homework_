from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home_page() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def page_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def page_user(user_id: str) -> dict:
    return {'message': f'Вы воошли как пользователь № {user_id}'}

@app.get('/user')
async def info_user(username: str, age: int) -> dict:
    return {'message': f'Информация о ползователе. Имя: {username}, Возраст: {age}'}
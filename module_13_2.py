from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text = ['/start'])
async def start(mmessage):
    print('Привет! Я бот помогающий твоему здоровью')

@dp.message_handler(text = ['Urban', 'god'])
async def urban_message(message):
    print('Urban message')

@dp.message_handler(text = ['start'])
async def start_message(message):
    print('Start message')

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
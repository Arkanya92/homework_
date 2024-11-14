import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for number in range(1, 6):
        speed = 1 / power
        await asyncio.sleep(speed)
        print(f'Силач {name} поднял {number}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    print('Старт соревнования!')
    athlete_1 = asyncio.create_task(start_strongman('Pasha', 3))
    athlete_2 = asyncio.create_task(start_strongman('Denis', 4))
    athlete_3 = asyncio.create_task(start_strongman('Apolon', 5))
    await athlete_1
    await athlete_2
    await athlete_3
    print('Конец соревнования!')


asyncio.run(start_tournament())
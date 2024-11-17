import asyncio


async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, power + 1):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Denis', 3))
    task2 = asyncio.create_task(start_strongman('Jane', 4))
    task3 = asyncio.create_task(start_strongman('Mari', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())

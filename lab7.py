import asyncio
#gjjjjjj
async def task1():
    print("Выполняется задача 1")
    await asyncio.sleep(1)  # Эмулируем длительную операцию
    print("Задача 1 завершена")

async def task2():
    print("Выполняется задача 2")
    await asyncio.sleep(2)
    print("Задача 2 завершена")

async def task3():
    print("Выполняется задача 3")
    await asyncio.sleep(0.5)
    print("Задача 3 завершена")

async def main():
    # Выполнение задач по порядку
    await task1()
    await task2()
    await task3()

asyncio.run(main())


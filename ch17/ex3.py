# Tasks
import asyncio

async def greet():
    print("Hi!")
    await asyncio.sleep(1)
    print("Hello!")
    await asyncio.sleep(2)
    print("How are you?")

coro = greet()


async def main():
    task = asyncio.create_task(coro)
    result = await task 
    print(result)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())

# grouping with async.gather()
async def main():
    results = await asyncio.gather(coro, coro)
    print(results)

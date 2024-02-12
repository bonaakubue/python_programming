# The await keyword
import asyncio

async def greeting():
    print("Hello there!")
    await asyncio.sleep(1)
    print('How are you?')

coro = greeting()
loop = asyncio.new_event_loop()
loop.run_until_complete(coro)
loop.close()


#multiple awaits
async def greet():
    print("Hi!")
    await asyncio.sleep(1)
    print("Hello!")
    await asyncio.sleep(2)
    print("How are you?")

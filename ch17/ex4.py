# Futures

import asyncio
async def greeting(future):
    await asyncio.sleep(1)
    result = "Hello there!"
    future.set_result(result)

async def main():
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    loop.create_task(greeting(fut))
    await fut
    print(fut.result())

loop = asyncio.new_event_loop()
loop.run_until_complete(main())

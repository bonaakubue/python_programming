# asyncio module

import asyncio
async def greet():
    print("Hello there!")

coro = greet()

#execute
asyncio.run(greet())

# Create an event loop
loop = asyncio.new_event_loop()

# Run the coroutine within the event loop
loop.run_until_complete(coro)

# Close the event loop
loop.close()

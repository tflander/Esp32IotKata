import time
import asyncio

async def show(string, delayInSeconds):
    print(string, delayInSeconds)
    time.sleep(delayInSeconds)
    return await string

show("foo", 2)
asyncio.ensure_future(show("foo", 2))
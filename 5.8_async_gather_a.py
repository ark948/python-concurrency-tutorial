# the following uses async.gather() to run two asynchronous operations and display the result

import asyncio

async def call_api(message, result, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    a, b = await asyncio.gather(
        call_api('Calling API 1...', 100, 1),
        call_api('Calling API 2...', 200, 1)
    )
    
    print(a, b)

asyncio.run(main())
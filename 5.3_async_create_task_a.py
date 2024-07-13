import asyncio
import time

async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result

async def main():
    start = time.perf_counter()

    price = await call_api('Get stock price of GOOG...', 300)
    print(price)

    price = await call_api('GET stock price of APPL...', 400)
    print(price)

    end = time.perf_counter()
    print(f'It took {round(end-start, 0)} second(s) to complete.')


# this code is synchronous but does not run concurrently
# to run multiple operations concurrently, we need to use tasks
asyncio.run(main())
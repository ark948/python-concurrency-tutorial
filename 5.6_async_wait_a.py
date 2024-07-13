import asyncio
from asyncio import create_task


class APIError(Exception):
    pass


async def call_api(message, result=100, delay=3, raise_exception=False):
    print(message)
    await asyncio.sleep(delay)
    if raise_exception:
        raise APIError
    else:
        return result


async def main():
    task_1 = create_task(call_api('calling API 1...', result=1, delay=1))
    task_2 = create_task(call_api('calling API 2...', result=2, delay=2))
    task_3 = create_task(call_api('calling API 3...', result=3, delay=3))

    pending = (task_1, task_2, task_3)

    while pending:
        done, pending = await asyncio.wait(
            pending,
            return_when=asyncio.FIRST_COMPLETED
        )
        result = done.pop().result()
        print(result)


asyncio.run(main())
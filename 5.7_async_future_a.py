from asyncio import Future
import asyncio


async def plan(my_future):
    print('Planning my future...')
    await asyncio.sleep(1)
    my_future.set_result('Bright')


def create() -> Future:
    my_future = Future()
    asyncio.create_task(plan(my_future))
    return my_future


async def main():
    my_future = create()
    result = await my_future

    print(result)


asyncio.run(main())
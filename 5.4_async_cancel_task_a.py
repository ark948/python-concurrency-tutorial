# sometimes, if an async task took longer than necessary, there would be way to cancel it
# also there would be no visible result

# cancel() method is the only solution

# the following example shows how to cancel a task, if a certain amount of time has passed
import asyncio
from asyncio import CancelledError


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    task = asyncio.create_task(call_api('Calling API...', result=2000, delay=5))

    time_elapsed = 0
    while not task.done():
        time_elapsed += 1
        await asyncio.sleep(1)
        print('Task has not completed, checking again in a second')
        if time_elapsed == 3:
            print('Cancelling the task...')
            task.cancel()
            break

    try:
        await task
    except CancelledError:
        print('Task has been cancelled.')


asyncio.run(main())
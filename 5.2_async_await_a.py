# a coroutine is a function with the ability to pause execution...
# when encountering an operation that may take a while to complete

# async -> creates a coroutine
# await -> pauses a coroutine

# a simple function
def square(number: int) -> int:
    return number*number

result = square(10)
# print(result)

# the same function but now a coroutine
async def square2(number: int) -> int:
    return number*number

# calling it will return a coroutine object
result2 = square2(10)
# print(result2)
# running this will result to an error, coroutine 'square2' was never awaited

# to run a coroutine, it must go into an event loop, -> was done manually in python 3.7 and prior

# with asyncio -> automatically create an event loop, run a coroutine, and close it

# continue on 5.2_async_await_b.py
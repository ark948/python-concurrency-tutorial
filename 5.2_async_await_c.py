import asyncio

async def square(number: int) -> int:
    return number * number

async def main() -> None:
    # await must get the result of an async function which is a coroutine
    x = await square(10)
    print(f'x={x}')

    y = await square(5)
    print(f'y={y}')

    print(f'total={x+y}')

if __name__ == '__main__':
    asyncio.run(main())
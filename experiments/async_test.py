import asyncio
import time

async def say_hello():
    print("Hello_async")
    await asyncio.sleep(5)
    print("World_async")

def say_hello_normal():
    print("Hello")
    time.sleep(5)
    print("World")

async def main():
    # Run 3 say_hello coroutines concurrently
    await asyncio.gather(say_hello(), say_hello(), say_hello())

    # Run 3 say_hello coroutines sequentially
    await say_hello()
    await say_hello()
    await say_hello()

if __name__ == "__main__":
    say_hello_normal()       # Run synchronous version first
    asyncio.run(main())      # Run async code once
    say_hello_normal()       # Run synchronous version last

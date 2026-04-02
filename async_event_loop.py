import asyncio
import time
import future


async def get_result(future):
    await asyncio.sleep(5)
    future.set_result("...a future result")
    
async def main():
    my_future = asyncio.Future()
    task1 = asyncio.create_task(get_result(my_future))
    await task1
    print("I'm waiting for ...")
    print(await my_future)
    print("Before continuing with other tasks...")
    
asyncio.run(main())


# Event loop

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
    
    
### Asynchronous iterations with and without async for
# this is not running concurrently
async def gen(n):
    for i in range(n):
        await asyncio.sleep(1)
        yield i
        
async def main():
    async for i in gen(10):
        print(i)
        
asyncio.run(main())

# asyn as completed

async def f(i):
    print(f"start iteration step {i}")
    await asyncio.sleep(i)
    print(f"end iteration step {i}")
    return i

async def main():
    t1 = time.perf_counter()
    for j in asyncio.as_completed([f(i) for i in range(10)]):
        result = await j
        print(f"Result: {result}")
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1} seconds!")    
asyncio.run(main())


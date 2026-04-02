
#%%
import asyncio
import time
import future

  
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


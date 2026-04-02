import asyncio
import time
import future


## gathering awaitable for concurrent execution

async def corountine(t, id):
    await asyncio.sleep(t)
    print(f"I am the corountine {id} and I slept for {t} seconds!")
    return t +2

async def main():
    t1 = time.perf_counter()
    results = await asyncio.gather(
        corountine(10, "A"),
        corountine(4, "B"),
        corountine(1, "C")
    )
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1} seconds!")
    print(f"Results: {results}")
    
asyncio.run(main())

# ACHIEVING SAME RESULT WITH TASKS
async def main():
    t1 = time.perf_counter()
    task1 = asyncio.create_task(corountine(10, "A"))
    task2 = asyncio.create_task(corountine(4, "B"))
    task3 = asyncio.create_task(corountine(1, "C"))
    r1 = await task1
    r2 = await task2
    r3 = await task3
    results = [r1, r2, r3]
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1} seconds!")
    print(f"Results: {results}")
    
asyncio.run(main())


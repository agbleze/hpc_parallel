


## Async Queue
import asyncio
import time
import future
import random

async def producer(name, queue):
    n = random.randint(0, 10)
    await asyncio.sleep(n)
    await queue.put(n)
    print(f"Producer {name} added {n} to queue")
    
    
async def consumer(name, queue):
    while True:
        n = await queue.get()
        await asyncio.sleep(n)
        print(f"Consumer {name} got {n} from queue")
        queue.task_done()
        
async def main(nproducers, nconsumers):
    q = asyncio.Queue()
    producers = [asyncio.create_task(producer(n, q)) for n in range(nproducers)]
    consumers = [asyncio.create_task(consumer(n, q)) for n in range(nconsumers)]
    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()
        
asyncio.run(main(5, 3))
    
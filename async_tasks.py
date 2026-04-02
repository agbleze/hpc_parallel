import asyncio
import time
import future


# %%  ### create Task 
async def other_task():
    print("I am a task!")
    
async def main_task():
    task = asyncio.create_task(other_task())
    print("Awaiting for...")
    await asyncio.sleep(1)
    await task
    print("--. AsyncIO Task")
    
asyncio.run(main_task())                                                    

#%% task
import time
async def other_task(id,t):
    await asyncio.sleep(t)
    print(f"I am a task {id} and I slept for {t} seconds!")
    
async def main_task():
    t1 = time.perf_counter()
    task1 = asyncio.create_task(other_task(1, 10))
    task2 = asyncio.create_task(other_task(2, 4))
    task3 = asyncio.create_task(other_task(3, 1))
    await task1
    await task2
    await task3
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1} seconds!")
    
    
asyncio.run(main_task())
    
# without creating task, the execution is sequential and the total time is the sum of the time of each coroutine

async def other_task(id,t):
    await asyncio.sleep(t)
    print(f"I am a task {id} and I slept for {t} seconds!")
    
async def main_task():
    t1 = time.perf_counter()
    await other_task(1, 10)
    await other_task(2, 4)
    await other_task(3, 1)
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1} seconds!")

asyncio.run(main_task())


# seting and getting task name
async def other_task(t):
    await asyncio.sleep(t)
    id = asyncio.current_task().get_name()
    print(f"I am a coroutine {id} and I slept for {t} seconds!")
    
async def main_task():
    t1 = time.perf_counter()
    task1 = asyncio.create_task(other_task(10), name="Task 1")
    task2 = asyncio.create_task(other_task(4), name="Task 2")
    task3 = asyncio.create_task(other_task(1), name="Task 3")
    await task1
    await task2
    await task3
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1} seconds!")
    
asyncio.run(main_task())

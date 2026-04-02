
import asyncio
import time
import future



##### FUTURES 

async def get_result(result):
    await asyncio.sleep(5)
    result = "...an awaited result..."
    
async def main():
    my_result = ""
    task1 = asyncio.create_task(get_result(my_result))
    await task1
    print("I'm wating for ...")
    print(my_result)
    
    
asyncio.run(main())

# this fixes the code above so that the result is eventually printed after the task is completed
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


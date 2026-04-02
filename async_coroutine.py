import asyncio
import time
import future


async def main():
    print("I am a coroutine!")
    await asyncio.sleep(1)
    await other()
    print("--. AsyncIO")
# %%

async def other():
    print("I am another corountine!")
# %%
asyncio.run(main())
import asyncio
import time

def function_sync():
    print("Hello from sync function")
    time.sleep(1)
    print("Goodbye from sync function")
    
async def function_async():
    print("Hello from async function")
    await asyncio.sleep(1)
    print("Goodbye from async function")
    
    
async def main():
    coroutines = [function_async() for _ in range(5)]
    await asyncio.gather(*coroutines)

start = time.time()
asyncio.run(main())
print(f"Async functions took {time.time() - start:.2f} seconds")

function_sync()
function_sync()
print(f"Sync functions took {time.time() - start:.2f} seconds")
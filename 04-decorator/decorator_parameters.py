import time
from typing import Any

def measure_execution_time(func):
    def wrapper(*args: Any, **kwargs: Any):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.8f} seconds")
    return wrapper

@measure_execution_time
def travel_cycle(maxRange:int):
    for i in range(maxRange):
        print(i)
        time.sleep(1)
        
travel_cycle(5)
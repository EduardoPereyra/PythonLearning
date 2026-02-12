import time

def measure_execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start:.8f} seconds")
    return wrapper

@measure_execution_time
def travel_cycle():
    for i in range(5):
        print(i)
        time.sleep(1)
        
travel_cycle()
from scoop import futures
import time
import math


def worker(value):
    time.sleep(10)
    print(f"I am the worker {value}")
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    list(futures.map(worker, range(4)))
    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time} seconds")
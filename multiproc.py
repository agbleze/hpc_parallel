
#%%
import multiprocessing
import time
import os

# %%
def function(i):
    pid = os.getpid()
    print(f"start process {pid}")
    time.sleep(2)
    print(f"end process {pid}")
    #return

p1 = multiprocessing.Process(target=function, args=(1,))
p2 = multiprocessing.Process(target=function, args=(2,))
p3 = multiprocessing.Process(target=function, args=(3,))
p4 = multiprocessing.Process(target=function, args=(4,))
p5 = multiprocessing.Process(target=function, args=(5,))

p1.start()
p2.start() 
p3.start()
p4.start()
p5.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
print("END program")  
    
# %% automating the loop for function
processes = []
n_proc = 5

for i in range(n_proc):
    p = multiprocessing.Process(target=function, args=(i,))
    processes.append(p)
    p.start()
    
for i in range(n_proc):
    processes[i].join()
print("END Program")

# %% #######  Processing Pool #######
import multiprocessing
import time

def function(i):
    process = multiprocessing.current_process()
    print("start process %i(pid:%s)" %(i, process.pid))
    time.sleep(2)
    print("end Process %i(pid:%s)" %(i, process.pid))
    return 

pool = multiprocessing.Pool()
print("Processes started: %s" %pool._processes)
for i in range(pool._processes):
    results = pool.apply(function, args=(i,))
pool.close()
print("END Program")


#%% Specifying the number of processes in the pool

def function(i):
    process = multiprocessing.current_process()
    print("start Task %i(pid:%s)" %(i, process.pid))
    time.sleep(2)
    print("end Task %i(pid:%s)" %(i, process.pid))
    return

pool = multiprocessing.Pool(processes=4)
print("Processes started: %s" %pool._processes)
for i in range(12):
    results = pool.apply(function, args=(i,))
pool.close()
print("END Program")
    

# %% Subclassing  
from multiprocessing import Process
import time
import random

class ChildProcess(Process):
    def __init__(self, count):
        super().__init__()
        self.count = count
        
    def run(self):
        print("start Process %s" %self.count)
        time.sleep(2)
        print("end Process %s" %self.count)
        
        
processes = []
n_proc = 5

for i in range(n_proc):
    p = ChildProcess(i)
    processes.append(p)
    p.start()
    
for i in range(n_proc):
    processes[i].join()
# %% #### Communication channels - Queues   
from multiprocessing import Process, Queue
import time
import random

class Consumer(Process):
    def __init__(self, count, queue):
        super().__init__()
        self.count = count
        self.queue = queue
        
    def run(self):
        for i in range(self.count):
            local = self.queue.get()
            time.sleep(2)
            print("consumer has used this: %s" %local)
            
            
class Producer(Process):
    def __init__(self, count, queue):
        super().__init__()
        self.count = count
        self.queue = queue
        
    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
    
    def run(self):
        for i in range(self.count):
            local = self.request()
            self.queue.put(local)
            print("producer has produced this: %s" %local)
        

queue = Queue()
count = 5
p1 = Producer(count, queue)
p2 = Consumer(count, queue)
p1.start()
p2.start()
p1.join()
p2.join()


# %%  #### Pipe
from multiprocessing import Process, Pipe
import time
import random

class Consumer(Process):
    def __init__(self, count, conn):
        super().__init__()
        self.count = count
        self.conn = conn
        
    def run(self):
        for i in range(self.count):
            local = self.conn.recv()
            time.sleep(2)
            print("consumer has used this: %s" %local)
            

class Producer(Process):
    def __init__(self, count, conn):
        super().__init__()
        self.count = count
        self.conn = conn
        
    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
    
    def run(self):
        for i in range(self.count):
            local = self.request()
            self.conn.send(local)
            print("producer has produced this: %s" %local)
            
            
recver, sender = Pipe()
count = 5
p1 = Producer(count, sender)
p2 = Consumer(count, recver)

p1.start()
p2.start()
p1.join()
p2.join()
recver.close()
sender.close()
# %% # mapping functions to Pool Processes
import time
import math
import numpy as np
from multiprocessing.pool import Pool

def func(value):
    result = math.sqrt(value)
    print("The value %s and the elaboration is %s" %(value, result))
    time.sleep(value)
    return result


with Pool() as pool:
    data = np.array([1, 2, 3, 4, 5])
    results = pool.map(func, data)
    print("The map process is going on...")
    for result in results:
        print("This is the result: %s" %result)
    print("END Program")

# %% usimg the map_async function

with Pool() as pool:
    data = np.array([1, 2, 3, 4, 5])
    results = pool.map_async(func, data)
    print("The map process is going on...")
    for result in results.get():
        print("This is the result: %s" %result)
    print("END Program")

# %% ## using chuncksize to specify of elements form each iterable to assign to each process

with Pool() as pool:
    data = np.array([np.random.randint(1, 100) for _ in range(200)])
    results = pool.map(func, data, chunksize=4)
    print("The main process is going on...")
    for result in results:
        print("This is the result: %s" %result)
    print("END Program")
    
# %%  ##### ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(10) as executor:
    data = np.array([np.random.randint(1, 100) for _ in range(20)])
    for result in executor.map(func, data):
        print("This is the result: %s" %result)
    print("END Program")
# %% ### Using ProcessPoolExecutor with chuncksize
import time
import math
import os
import numpy as np
from concurrent.futures import ProcessPoolExecutor

def func(value):
    result = math.sqrt(value)
    pid = os.getpid()
    print("[Pid:%s] The value %s and the elaboration is %s" %(pid, value, result))
    time.sleep(value)
    return result


with ProcessPoolExecutor(10) as executor:
    data = np.array([np.random.randint(1, 100) for _ in range(20)])
    for result in executor.map(func, data, chunksize=4):
        print("This is the result: %s" %result)
    print("END Program")
# %%


#%%
import os
import sys
import time
from glob import glob
from pathlib import Path
# %%
cwd = os.getcwd()
# %%
cwd_path = Path(cwd) 
# %%
rflies = cwd_path.rglob('*.pdf')
# %%
all_files = list(rflies)
# %%
all_files[0].name
# %%
names = [f.name for f in all_files]
# %%
names
# %%
len(names)
# %%
(1)/(1-0.9)
# %%
import threading
import time


#%%
def function(i):
    print("Start Thread %i\n" %i)
    time.sleep(2)
    print(f"End Thread %i\n" %i)
    return
#%% Thread()

t1 = threading.Thread(target=function, args=(1,))
t2 = threading.Thread(target=function, args=(2,))
t3 = threading.Thread(target=function, args=(3,))
t4 = threading.Thread(target=function, args=(4,))
t5 = threading.Thread(target=function, args=(5,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print("END program")
# %% join()
t1 = threading.Thread(target=function, args=(1,))
t2 = threading.Thread(target=function, args=(2,))
t3 = threading.Thread(target=function, args=(3,))
t4 = threading.Thread(target=function, args=(4,))
t5 = threading.Thread(target=function, args=(5,))
t1.start()
t2.start()
t3.start()  
t4.start()
t5.start()
t1.join()
t2.join()
print("First set of threads done")
[i for i in range(100_000_000)]
print("The program can execute other code here")
t3.join()
t4.join()
t5.join()
print("Second set of threads done")
print("END program")
# %%  Thread Synchronization pattern
n_threads = 5
threads = []

for i in range(n_threads):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    
for i in range(n_threads):
    threads[i].join()

# %% # ThreadPoolExecutor provides  high-level interface for asynchronously executing callables.
import concurrent.futures

def thread(num, t):
    print("Thread %s started" %num)
    time.sleep(t)
    print("Thread %s ended" %num)
    
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as t:
    t.submit(thread(1, 10))
    t.submit(thread(2, 1))
    t.submit(thread(3, 10))
    t.submit(thread(4,4))
    print("Program ended")

# %%
t1 = threading.Thread(target=thread, args=(1,10,))
t2 = threading.Thread(target=thread, args=(2,1,))
t3 = threading.Thread(target=thread, args=(3,10,))
t4 = threading.Thread(target=thread, args=(4,4,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("Program ended")
# %% Thread competition
import threading
import time
sequence = ""
COUNT = 5
timeA = 5
timeB = 10

def addA():
    global sequence
    for i in range(COUNT):
        time.sleep(timeA)
        sequence = "%sA" %sequence
        print("Sequence: %s" %sequence)
        
def addB():
    global sequence
    for i in range(COUNT):
        time.sleep(timeB)
        sequence = "%sB" %sequence
        print("Sequence: %s" %sequence)
        
t1 = threading.Thread(target=addA)
t2 = threading.Thread(target=addB)
t1.start()
t2.start()
t1.join()
t2.join()

# %% Thread Subclass
from threading import Thread

class ThreadA(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global sequence
        for i in range(COUNT):
            time.sleep(timeA)
            sequence = "%A" %sequence
            print("Sequence: %s" %sequence)
            
class ThreadB(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global sequence
        for i in range(COUNT):
            time.sleep(timeB)
            sequence = "%sB" %sequence
            print("Sequence: %s" %sequence)

t1 = ThreadA()
t2 = ThreadB()
t1.start()
t2.start()
t1.join()
t2.join()

# %%
class ThreadA(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global sequence
        for i in range(COUNT):
            time.sleep(timeA)
            sequence = "%sA" %sequence
            print("Sequence: %s" %sequence)
class ThreadB(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global sequence
        for i in range(COUNT):
            time.sleep(timeB)
            sequence = "%sB" %sequence
            print("Sequence: %s" %sequence)
# the Main program
t1 = ThreadA()
t2 = ThreadB()
t1.start()
t2.start()
t1.join()
t2.join()
# %% Synchronization with Locks
# the two function will compete for the shared data and 
# the result will be unpredictable. 
# Given the race condition, the final value of the shared data can be different each time we run the program.
shared_data = 0

def funcA():
    global shared_data
    for i in range(10):
        local = shared_data
        local += 10
        time.sleep(1)
        shared_data = local
        print("Thread A wrote: %s \n" %shared_data)
        
def funcB():
    global shared_data
    for i in range(10):
        local = shared_data
        local -= 10
        time.sleep(1)
        shared_data = local
        print("Thread B wrote: %s \n" %shared_data)
        
        
t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)
t1.start()
t2.start()
t1.join()
t2.join()

# %% Using Locks to sychronize and avoid race conditions

shared = 0
lock = threading.Lock()

def funcA():
    global shared
    for i in range(10):
        lock.acquire()
        local = shared
        local += 10
        time.sleep(1)
        shared = local
        print("Thread A wrote: %s, %i \n" %(shared, i))
        lock.release()
        lock.acquire()
        
def funcB():
    global shared
    for i in range(10):
        lock.acquire()
        local = shared
        local -= 10
        time.sleep(1)
        shared = local
        print("Thread B wrote: %s, %i \n" %(shared, i))
        lock.release()
        
        
t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)

t1.start()
t2.start()
t1.join()
t2.join()

# %% Context manager for locks

shared = 0
lock = threading.Lock()

def funcA():
    global shared
    for i in range(10):
        with lock:
            local = shared
            local += 10
            time.sleep(1)
            shared = local
            print("Thread A wrote: %s, %i \n" %(shared, i))
            
def funcB():
    global shared
    for i in range(10):
        with lock:
            local = shared
            local -= 10
            time.sleep(1)
            shared = local
            print("Thread B wrote: %s, %i \n" %(shared, i))
            
            
t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)
t1.start()
t2.start()
t1.join()
t2.join()


# %% # Reentrant Locks (RLocks) allow a thread to acquire the same lock multiple times without causing a deadlock.
import threading
import time

shared = 0
rlock = threading.RLock()

def func(name, t):
    global shared
    for i in range(3):
        rlock.acquire()
        local = shared
        time.sleep(t)
        for j in range(2):
            rlock.acquire()
            local += 1
            time.sleep(2)
            shared = local
            print("Thread %s-%s wrote: %s" %(name, j, shared))
            rlock.release()
        shared = local + 1
        print("Thread %s wrote: %s" %(name, shared))
        rlock.release()
        

t1 = threading.Thread(target=func, args=("A", 2))
t2 = threading.Thread(target=func, args=("B", 10))
t3 = threading.Thread(target=func, args=("C", 1))
t1.start()
t2.start()  
t3.start()
t1.join()
t2.join()
t3.join()

#%% Semaphore is a synchronization primitive that allows a certain number of threads to access a shared resource concurrently. 
# It maintains a counter that is decremented when a thread acquires the semaphore and incremented when a thread releases it. If the counter reaches zero, any additional threads that attempt to acquire the semaphore will block until another thread releases it.

from threading import Thread, Semaphore
import time
import random

semaphore = Semaphore(1)
shared = 1
count = 5

class consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        global semaphore
        self.count = count
        
    def run(self):
        global shared
        for i in range(self.count):
            semaphore.acquire()
            print("consumer has used this: %s" %shared)
            shared = 0
            semaphore.release()
            
class producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count
        global semaphore
        
    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
    
    def run(self):
        global shared
        for i in range(self.count):
            semaphore.acquire()
            shared = self.request()
            print(("producer has loaded this: %s" %shared))
            semaphore.release()
            
t1 = producer(count)
t2 = consumer(count)
t1.start()
t2.start()
t1.join()
t2.join()

# this has the problem of the producer generating all it values from 
# the iteration before the consumer starts to consumer only the last generate value.
# %% we want a case where producer generates a value and the consumer consumes it 
# before the producer generates the next value.

from threading import Thread, Semaphore
import time
import random


semaphore = Semaphore(1)
shared = 1
count = 5

def request():
    time.sleep(1)
    return random.randint(0, 100)

class consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        global semaphore
        self.count = count
        
    def run(self):
        global shared
        for i in range(self.count):
            semaphore.acquire()
            print("consumer has used this: %s" %shared)
            shared = 0
    
class producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count
        global semaphore
        
    def run(self):
        global shared
        for i in range(self.count):
            shared = request()
            print(("producer has loaded this: %s" %shared))
            semaphore.release()
            
t1 = producer(count)
t2 = consumer(count)
t1.start()
t2.start()  
t1.join()
t2.join()

# first to access shared resource is the consumer hence consumers the default value instead of value generated by producer
# %%

from threading import Thread, Semaphore
import time
import random
semaphore = Semaphore(0)
shared = 1  
count = 5

def request():
    time.sleep(1)
    return random.randint(0, 100)

class consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        global semaphore
        self.count = count
        
    def run(self):
        global shared
        for i in range(self.count):
            semaphore.acquire()
            print("consumer has used this: %s" %shared)
            shared = 0
            
class producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count
        global semaphore
        
    def run(self):
        global shared
        for i in range(self.count):
            shared = request()
            print(("producer has loaded this: %s" %shared))
            semaphore.release() 
            
t1 = producer(count)
t2 = consumer(count)
t1.start()
t2.start()
t1.join()
t2.join()

# this correct implementation ensures that producer first generate a value and consumer consumes it, and this alternation continues 
# %% Condition as synchronization primitive that allows threads to wait for certain conditions to be met before proceeding with their execution.
# A condition variable is associated with a lock and provides methods for threads to wait for specific conditions to be met and to notify other threads when those conditions are met.

from threading import Thread, Condition
import time
import random


condition = Condition()
shared = 1
count = 5


class Consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        global condition
        self.count = count
        
    def run(self):
        global shared
        for i in range(self.count):
            condition.acquire()
            if shared == 0:
                condition.wait()
            print("Consumer has used this: %s" %shared)
            shared = 0
            condition.notify()
            condition.release()
            
class Producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count
        global condition
        
    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
    
    def run(self):
        global shared
        for i in range(self.count):
            condition.acquire()
            shared = self.request()
            print("Producer has loaded this: %s" %shared
                  )
            condition.wait()
            if shared == 0:
                condition.notify()
            condition.release()
            
t1 = Producer(count)
t2 = Consumer(count)    
t1.start()
t2.start()
t1.join()
t2.join()




# %%
from threading import Thread, Condition
import time
import random

condition = Condition()
shared = None
count = 5


class Consumer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
        
    def run(self):
        global shared
        for _ in range(self.count):
            with condition:
                while shared is None:
                    condition.wait()
                print("Consumer used:", shared)
                shared = None
                condition.notify()


class Producer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
        
    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
    
    def run(self):
        global shared
        for _ in range(self.count):
            with condition:
                while shared is not None:
                    condition.wait()
                shared = self.request()
                print("Producer loaded:", shared)
                condition.notify()
                
                
t1 = Producer(count)
t2 = Consumer(count)
t1.start()
t2.start()
t1.join()
t2.join()

# %% Event is a synchronization primitive that allows threads to wait for specific events to occur before proceeding with their execution. 
# An event can be set or cleared, and threads can wait for the event to be set before continuing.

from threading import Thread, Event
import time
import random

event = Event()
shared = 1
count = 5

class Consumer(Thread):
    def __init__(self, count):
        super().__init__()
        global event
        self.count = count
        
    def run(self):
        global shared
        for i in range(self.count):
            event.wait()
            print("Consumer has used this: %s" %shared)
            shared = 0
            event.clear()

class Producer(Thread):
    def __init__(self, count): 
        super().__init__()
        self.count = count
        global event
        
    def request(self):
        #time.sleep(1)
        return random.randint(0, 100)
    
    def run(self):
        global shared
        for i in range(self.count):
            shared = self.request()
            print("Producer has loaded this: %s" %shared)
            event.set()
            
            
t1 = Producer(count)
t2 = Consumer(count)
t1.start()
t2.start()
t1.join()
t2.join()

# %% Using multiple consumer and producer threads 
# without proper synchronization can lead to disordered results

from threading import Thread, Event
import time
import random

event = Event()
shared = 1
count = 5

class Consumer(Thread):
    def __init__(self, count):
        super().__init__()
        global event
        self.count = count
    
    def run(self):
        global shared
        for i in range(self.count):
            event.wait()
            print("consumer has used this: %s" %shared)
            shared = 0
            event.clear()
class Producer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
        
    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
    
    def run(self):
        global shared
        for i in range(self.count):
            shared = self.request()
            print("producer has loaded this: %s" %shared)
            event.set()
            
t1 = Producer(count)
t2 = Producer(count)
t3 = Consumer(count)
t4 = Consumer(count)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

# %% Queue is a thread-safe data structure that allows multiple threads to safely access and modify a shared queue of items.
from threading import Thread
from queue import Queue
import time
import random

queue = Queue()
shared = 1
count = 5

class Consumer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
        
    def run(self):
        global queue
        for i in range(self.count):
            local = queue.get()
            print("Consumer has used this: %s \n" %local)
            queue.task_done()
            
class Producer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
        
    def request(self):
        time.sleep(1)
        return random.randint(0, 100)

    def run(self):
        global queue
        for i in range(self.count):
            local = self.request()
            queue.put(local)
            print("Producer has loaded this: %s \n" %local)
            
            
t1 = Producer(count)
t2 = Producer(count)
t3 = Consumer(count)
t4 = Consumer(count)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

# %%

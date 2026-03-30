
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

# %%

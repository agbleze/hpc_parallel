
#%%
import numpy as np
import time
from numba import cuda

@cuda.jit
def add_one(a):
    tx = cuda.threadIdx.x
    ty = cuda.blockIdx.x
    dim = cuda.blockDim.x
    
    pos = tx + ty * dim
    if pos < a.size:
        a[pos] += 1
        
#%%        
n = 10
a_host = np.random.random(n)
print(f"Vector a: {a_host}")
a_dev = cuda.to_device(a_host)

#%%
threadsperblock = 128
blockspergrid = (a_host.size // threadsperblock) +1

add_one[threadsperblock, blockspergrid](a_dev)
a_host = a_dev.copy_to_host()
print(f"New Vector a: {a_host}")


# %%  Alternative way of defining thread geometry

host_data = np.random.random(10)
device_data = cuda.to_device(host_data)

@cuda.jit
def increment_by_one(a):
    pos = cuda.grid(1)
    if pos < a.size:
        a[pos] += 1

increment_by_one[threadsperblock, blockspergrid](device_data)
result = device_data.copy_to_host()
print(f"Result: {result}")


## 2D matrix
import math

@cuda.jit
def add_one_2D(A):
    x, y = cuda.grid(2)
    if x < A.shape[0] and y < A.shape[1]:
        A[x, y] += 1
        
n = 4
A_host = np.random.random((n, n))
print(f"Matrix A:\n{A_host}")
A_dev = cuda.to_device(A_host)

threadsperblock = (128, 128)
blockspergridx = math.ceil(A_host.shape[0] / threadsperblock[0])
blockspergridy = math.ceil(A_host.shape[1] / threadsperblock[1])

blocks_per_grid = (blockspergridx, blockspergridy)

add_one_2D[threadsperblock, blocks_per_grid](A_dev)

A_host = A_dev.copy_to_host()
print(f"New Matrix A:\n{A_host}")


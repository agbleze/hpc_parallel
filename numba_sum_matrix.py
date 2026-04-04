## transfering data through queue is done with stream
# multiple matrices require an empty matrix to store the result

import numpy as np
from numba import cuda
import math

@cuda.jit
def add_one_2D(A, B, C):
    x, y = cuda.grid(2)
    if x < A.shape[0] and y < A.shape[1]:
        C[x, y] = A[x, y] + B[x, y]
        
n = 4
A_host = np.random.random((n, n))
B_host = np.random.random((n, n))
C_host = np.zeros((n, n))

print(f"Matrix A:\n{A_host}")
print(f"Matrix B:\n{B_host}")

stream = cuda.stream()
A_dev = cuda.to_device(A_host, stream=stream)
B_dev = cuda.to_device(B_host, stream=stream)
C_dev = cuda.to_device(C_host, stream=stream)

threadsperblock = (128, 128)
blockspergridx = math.ceil(A_host.shape[0] / threadsperblock[0])
blockspergridy = math.ceil(A_host.shape[1] / threadsperblock[1])

blocks_per_grid = (blockspergridx, blockspergridy)

add_one_2D[threadsperblock, blocks_per_grid](A_dev, B_dev, C_dev)

C_host = C_dev.copy_to_host(stream=stream)

print(f"Result Matrix C:\n{C_host}") 



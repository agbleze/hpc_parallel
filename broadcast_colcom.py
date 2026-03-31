from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data = np.random.randint(1, 10)
else:
    data = None
    
data = comm.bcast(data, root=0)

if rank == 1:
    print(f"The squaure of {data} is {data*data}")
if rank == 2:
    print(f"Half of {data} is {data/2}")
if rank == 3:
    print(f"Double of {data} is {data*2}")

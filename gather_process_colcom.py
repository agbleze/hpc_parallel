from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
data = 2*rank + 1
print(f"Process {rank} calculated this value {data}")
array = comm.gather(data, root=0)
if rank == 0:
    result = 0
    for i in range(0, size):
        result += array[i]
    print(f"The result of the parallel computation is {result}")
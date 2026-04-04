from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
if rank == 0:
    array = ["AAA", "BBB", "CCC", "DDD"]
else:
    array = None

data = comm.scatter(array, root=0)
print(f"Process {rank} is working on {data}")
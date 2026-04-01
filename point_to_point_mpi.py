# Point to point communication in MPI

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
print("The process %d is started" %rank)
if rank == 0:
    msg = "This is my message"
    receiver = 1
    comm.send(msg, dest=receiver)
    print(f"Process 0 sent {msg} to process {receiver}")
    
if rank == 1:
    source = 0
    msg = comm.recv(source=source)
    print(f"Process 1 received {msg} from process {source}")
    
    

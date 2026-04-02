from mpi4py import MPI
import sys
comm = MPI.COMM_WORLD
rank = comm.rank

comm_3D = comm.Create_cart(dims=[2,2,2],
                           periods=[False, False, False],
                           reorder=False
                           )

if comm_3D == MPI.COMM_NULL:
    print(f"Process {rank} is not part of the 2x2x2 Cartesian grid topology")
    sys.exit()
xyz = comm_3D.Get_coords(rank)
print(f"In this 3D topology, process {rank} has coordinates {xyz}")

right, left = comm_3D.Shift(0, 1)
up, down = comm_3D.Shift(1, 1)
forward, backward = comm_3D.Shift(2, 1)
print(f"Neighbors (left-right) {left, right}")
print(f"Neighbors (up-down) {up, down}")
print(f"Neighbors (forward-backward) {forward, backward}")

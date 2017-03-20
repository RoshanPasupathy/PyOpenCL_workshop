from helper import *
from definitions import *

import pyopencl as cl
import numpy
from time import time

# create context, queue and program
context = cl.create_some_context()
queue = cl.CommandQueue(context)
kernelsource = open("exercise4.cl").read()
program = cl.Program(context, kernelsource).build()

# A[N][N], B[N][N], C[N][N]
N = ORDER;          # ORDER taken from definitions.py file

# Number of elements in the matrix
size = N * N

# A matrix
h_A = numpy.empty(size).astype(numpy.float32)
h_A.fill(AVAL)      # AVAL taken from definitions.py file

# B matrix
h_B = numpy.empty(size).astype(numpy.float32)
h_B.fill(BVAL)      # BVAL taken from definitions.py file

# C matrix
h_C = numpy.empty(size).astype(numpy.float32)

# Create OpenCL buffers
d_a = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=h_A)
d_b =
d_c =

# Run kernel
h_C.fill(0.0)
start_time = time()

# Total work items (tuple)
globalrange =

# Number of work items in a work group (tuple)
localrange =

# Define scalar arg type list
arg_type_list = []

mmul = program.mmul
mmul.set_scalar_arg_dtypes(arg_type_list)
mmul(queue, globalrange, localrange, N, d_a, d_b, d_c)
queue.finish()

run_time = time() - start_time

# Return results
cl.enqueue_copy(queue, h_C, d_c)

results(N, h_C, run_time)

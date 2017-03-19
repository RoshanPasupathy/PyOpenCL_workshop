import numpy
import pyopencl as cl

from time import time

ITER = 16
N = 1024
# create context, queue and program
context = cl.create_some_context()
queue = cl.CommandQueue(context)
kernelsource = open("vector_iteradd.cl").read()
program = cl.Program(context, kernelsource).build()

# create host arrays
h_a = numpy.empty(N).astype(numpy.float32)
h_b = numpy.empty(N).astype(numpy.float32)
h_c = numpy.empty(N).astype(numpy.float32)

for i in range(N):
    h_a[i] = i
    h_b[i] = 2 * i

# create device buffers
mf = cl.mem_flags
d_a = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=h_a)
d_b = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=h_b)
d_c = cl.Buffer(context, mf.WRITE_ONLY, h_c.nbytes)

# run kernel
vadd = program.vadd
vadd.set_scalar_arg_dtypes([None, None, None, numpy.uint32])
workitems = (int(h_a.shape[0]/ITER),)
start_time = time()
vadd(queue, workitems, None, d_a, d_b, d_c, N)
run_time = time() - start_time

print("\nCompleted in %f9 s" % run_time)

# return results
cl.enqueue_copy(queue, h_c, d_c)

failure = 0
for i in range(N):
    if h_c[i] != h_a[i] + h_b[i]:
        failure = 1
if failure == 0:
    print("\nKernel successful! :D")
else:
    print("\nKernel unsuccessful :(")
        

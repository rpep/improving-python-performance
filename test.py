import numpy as np
from mylibrary import *
from timeit import default_timer

Nrepeats = 100
N = 100000000


def harness(method, repeats, N):
    a = np.random.rand(N).astype(np.float64)
    b = np.zeros_like(a)
 
    # Call once to remove any JIT overhead
    method(a, b)
 
    start = default_timer()

    for i in range(Nrepeats):
        method(a, b)

    duration = default_timer() - start
    print(f"{method.__name__} = {duration}")


methods = [
    mathematical_routine_numpy,
    mathematical_routine_numpy_faster,
    mathematical_routine_numba,
    mathematical_routine_c,
]

for method in methods:
    harness(method, Nrepeats, N)

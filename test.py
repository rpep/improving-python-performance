import numpy as np
import pandas as pd
from mylibrary import *
from timeit import default_timer

Nrepeats = 100
Nmin = 4
Nmax = 5

Ns = list(range(Nmin, Nmax))

def harness(method, repeats, N):
    a = np.random.rand(N).astype(np.float64)
    b = np.zeros_like(a)
 
    # Call once to remove any JIT overhead where relevant
    method(a, b)
 
    start = default_timer()

    for i in range(Nrepeats):
        method(a, b)

    duration = default_timer() - start
    return duration


methods = [
    mathematical_routine_numpy,
    mathematical_routine_numpy_faster,
    mathematical_routine_numba,
    mathematical_routine_c,
]

data = {"N": Ns}

for method in methods:
    times  = []
    for N in Ns:
        T = harness(method, Nrepeats, 10**N)
        times.append(T)
        print(f"10**{N}, {T}")

    data[method.__name__] = times

results = pd.DataFrame(data)

results.to_csv("results.csv")

import cython

cdef extern from "functions.h":
    void mathematical_routine(double* input, double* output, int N)


def mathematical_routine_c(double[:] input, double[:] output):
    assert len(input) == len(output)
    N = len(input)
    mathematical_routine(&input[0], &output[0], N)
 

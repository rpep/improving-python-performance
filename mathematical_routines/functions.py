import numpy as np
import numba

def mathematical_routine_numpy(input, output):
    output[:] = np.sqrt(input*input/12)


def mathematical_routine_numpy_faster(input, output):
    output[:] *= input*input
    output[:] /= 12
    np.sqrt(output, out=output)
    return output


@numba.njit(["void(float64[:], float64[:])"], parallel=True)
def mathematical_routine_numba(input, output):
    for i in numba.prange(input.shape[0]):
        output[i] = np.sqrt(input[i]*input[i]/12)

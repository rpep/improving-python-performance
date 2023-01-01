// Ryan Pepper (c) 2022
#include <math.h>

void mathematical_routine(double* input, double* output, int N) {
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        output[i] = sqrt(input[i]*input[i]/12);
    }
}

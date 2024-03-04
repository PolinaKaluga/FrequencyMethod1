import numpy as np


def get_fourier_coefficients_complex(func, T, N):
    c_n = lambda n: np.trapz([func(t) * np.exp(1j * 2 * np.pi * n * t / T) for t in np.linspace(0, T, 1000)],
                             np.linspace(0, T, 1000)) / T

    for n in range(1, N + 1):
        coefficient = c_n(n)
        print(f"N = {n}: c_{n} = {coefficient}")

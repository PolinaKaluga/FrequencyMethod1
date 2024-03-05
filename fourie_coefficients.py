import numpy as np
from function_graph import f

#выводим посчитанные фурье коэффициенты
def get_fourier_coefficients(func, T, N):
    for n in range(1, N + 1):
        a_n = 2/T * np.trapz([f(t) * np.cos(2*np.pi*n*t/T) for t in np.linspace(0, T, 1000)], np.linspace(0, T, 1000))
        b_n = 2/T * np.trapz([f(t) * np.sin(2*np.pi*n*t/T) for t in np.linspace(0, T, 1000)], np.linspace(0, T, 1000))
        print(f"N = {n}: a_{n} = {a_n}, b_{n} = {b_n}")


def get_fourier_coefficients_complex(func, T, N):
    c_n = lambda n: np.trapz([func(t) * np.exp(1j * 2 * np.pi * n * t / T) for t in np.linspace(0, T, 1000)],
                             np.linspace(0, T, 1000)) / T

    for n in range(1, N + 1):
        coefficient = c_n(n)
        print(f"N = {n}: c_{n} = {coefficient}")
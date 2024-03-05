import numpy as np
import matplotlib.pyplot as plt


def fourier_coefficients(func, T, N):
    c_n = lambda n: np.trapz([func(t) * np.exp(1j * 2 * np.pi * n * t / T) for t in np.linspace(0, T, 1000)], np.linspace(0, T, 1000)) / T
    return c_n

def fourier_series(t, c_n, T, N):
    sum = 0
    for n in range(-N, N + 1):
        sum += c_n(n) * np.exp(1j * 2 * np.pi * n * t / T)
    return sum

def plot_fourier_series_complex(func, T, N):
    c_n = fourier_coefficients(func, T, N)

    t = np.linspace(2, 10, 1000)
    y = [func(i) for i in t]
    z = [-fourier_series(i, c_n, T, N)+5  for i in t]

    plt.figure(figsize=(10, 5))
    plt.plot(t, y)
    plt.plot(t, z)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title("Частичная сумма Фурье G(t)   " + f'N = {N}')
    plt.grid()
    plt.legend()
    plt.show()
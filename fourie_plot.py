import numpy as np
import matplotlib.pyplot as plt



def fourier_coefficients(func, T, N):
    a_n = lambda n: 2/T * np.trapz([func(t) * np.cos(2*np.pi*n*t/T) for t in np.linspace(0, T, 1000)], np.linspace(0, T, 1000))
    b_n = lambda n: 2/T * np.trapz([func(t) * np.sin(2*np.pi*n*t/T) for t in np.linspace(0, T, 1000)], np.linspace(0, T, 1000))
    return a_n, b_n


def fourier_series(t, a_n, b_n, T, N):
    sum = 0
    for n in range(1, N + 1):
        sum += a_n(n) * np.cos(2 * np.pi * n * t / T) + b_n(n) * np.sin(2 * np.pi * n * t / T)
    return sum


def plot_fourier_series(func, T, N):
    a_n, b_n = fourier_coefficients(func, T, N)

    t = np.linspace(2, 10, 1000)
    y = [func(i) for i in t]
    z = [fourier_series(i, a_n, b_n, T, N) +2.5 for i in t]

    plt.figure(figsize=(10, 5))
    plt.plot(t, y)
    plt.plot(t, z)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(f'N = {N}')
    plt.grid()
    plt.legend()
    plt.show()
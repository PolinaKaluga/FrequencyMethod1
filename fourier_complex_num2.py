import numpy as np
import matplotlib.pyplot as plt

def real(t):
    T = 2
    R = 2
    real = -1
    t = (t + T / 8) % T - T / 8
    if (t >= -T/8 and t < T/8):
        real = R
    if (t >= T/8 and t < 3*T/8):
        real = (2*R - 8*R*t/T)
    if (t >= 3*T/8 and t < 5 *T/8):
        real = -R
    if (t >= 5*T/8 and t <= 7*T/8):
        real = -6*R + 8*R*t/T

    image = -1

    if (t >= -T/8 and t < T/8):
        image = 8*R*t/T
    if (t >= T/8 and t < 3*T/8):
        image = R
    if (t >= 3*T/8 and t < 5 *T/8):
        image = 4*R - 8*R*t/T
    if (t >= 5*T/8 and t <= 7*T/8):
            image = -R
    return real + image*1j

def fourier_coefficients(func, T, N):
    c_n = lambda n: np.trapz([func(t) * np.exp(1j * 2 * np.pi * n * t / T) for t in np.linspace(0, T, 1000)], np.linspace(0, T, 1000)) / T
    return c_n

def fourier_series(t, c_n, T, N):
    sum = 0
    for n in range(-N, N + 1):
        sum += c_n(n) * np.exp(1j * 2 * np.pi * n * t / T)
    return sum


# Функция для графика вещественной части
def plot_real_part(func, T, N):
    c_n = fourier_coefficients(func, T, N)

    t = np.linspace(0, T, 1000)
    y = [func(i) for i in t]
    z = [fourier_series(i, c_n, T, N) for i in t]

    plt.figure(figsize=(10, 5))
    plt.plot(np.real(t), np.real(y), label='Real Part of Original Function')
    plt.plot(np.real(t), np.real(z), label='Real Part of Fourier Series')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title("Fourier Series Approximation with Complex Coordinates (N = {})".format(N))
    plt.grid()
    plt.legend()
    plt.show()

# Функция для графика реальной части
def plot_imaginary_part(func, T, N):
    c_n = fourier_coefficients(func, T, N)

    t = np.linspace(0, T, 1000)
    y = [func(i) for i in t]
    z = [-fourier_series(i, c_n, T, N) for i in t]

    plt.figure(figsize=(10, 5))
    plt.plot(np.real(t), np.imag(y), label='Imaginary Part of Original Function')
    plt.plot(np.real(t), np.imag(z), label='Imaginary Part of Fourier Series')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title("Fourier Series Approximation with Complex Coordinates (N = {})".format(N))
    plt.grid()
    plt.legend()
    plt.show()
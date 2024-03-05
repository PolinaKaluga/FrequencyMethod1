import numpy as np
import matplotlib.pyplot as plt

def plot_complex_function():
    def real(t):
        T = 2
        R = 1
        t = (t + T / 8) % T - T / 8  #нужное значение периода
        result = np.zeros_like(t)
        for i in range(len(t)):
            if (t[i] >= -T/8 and t[i] < T/8):
                result[i] = R
            elif (t[i] >= T/8 and t[i] < 3*T/8):
                result[i] = (2*R - 8*R*t[i]/T)
            elif (t[i] >= 3*T/8 and t[i] < 5 *T/8):
                result[i] = -R
            elif (t[i] >= 5*T/8 and t[i] <= 7*T/8):
                result[i] = -6*R + 8*R*t[i]/T
            else:
                result[i] = 8*R*t[i]/T
        return result

    def im(t):
        T = 2
        R = 1
        t = (t + T / 8) % T - T / 8  #нужное значение периода
        result = np.zeros_like(t)
        for i in range(len(t)):
            if (t[i] >= -T/8 and t[i] < T/8):
                result[i] = 8*R*t[i]/T
            elif (t[i] >= T/8 and t[i] < 3*T/8):
                result[i] = R
            elif (t[i] >= 3*T/8 and t[i] < 5 *T/8):
                result[i] = 4*R -8*R*t[i]/T
            elif (t[i] >= 5*T/8 and t[i] <= 7*T/8):
                result[i] = -R
        return result

    # Определение периода функции T
    T = 2 # Например, период функции 2*pi

    # Создание массива точек времени от 0 до T с шагом 0.01
    t = np.arange(0, 10, 0.01)

    # Определение вещественной и мнимой частей функции f(t)
    real_part = real(t)
    imaginary_part = im(t)

    # Построение графика вещественной и мнимой частей на комплексной плоскости
    plt.figure()
    plt.plot(real_part, imaginary_part)
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.title('Complex Function Plot')
    plt.grid(True)
    plt.show()


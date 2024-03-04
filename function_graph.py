import matplotlib.pyplot as plt
import numpy as np

def f(t):
    if (t % 2 >= 0 and t % 2 < 1):
        return 2
    elif (t % 2 >= 1 and t % 2 < 2):
        return 3

def draw_function(func, x_min, x_max):
    x = np.linspace(x_min, x_max, 1000)
    y = [func(i) for i in x]

    # Plot the graph
    plt.figure(figsize=(10,6))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Периодическая функция')
    plt.grid(True)
    plt.show()




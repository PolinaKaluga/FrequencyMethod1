import numpy as np
from function_graph import *
from fourie_plot import *
from fourier_plot_complex import *
from fourie_coefficients import *
from fourie_coefficients_complex import *
T = 2 #период функции

#строим график функции

draw_function(f, 0, 4*np.pi)

#строим график суммы фурье f

plot_fourier_series(f, T, 4)

#строим график суммы фурье g

plot_fourier_series_complex(f, T, 3)

#находим коэф фурье

get_fourier_coefficients(f, T, 3)
get_fourier_coefficients_complex(f, 2, 3)
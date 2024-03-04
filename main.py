import numpy as np

from function_graph import draw_function
from function_graph import f
draw_function(f, 0, 4*np.pi)

T = 2 #период функции
#
# from fourie_plot import *
# plot_fourier_series(f, T, 3)

# from fourie_coefficients import *
# get_fourier_coefficients(f, T, 3)

from fourier_plot_complex import *
plot_fourier_series_complex(f, T, 3)

from fourie_coefficients_complex import *
get_fourier_coefficients_complex(f, 2, 3)
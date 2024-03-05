#пойдем по номерам



#1.строим график нашей функции

from function_graph import *
draw_function(f, 2, 10)

#2.вычисляем коэффициенты фурье

from fourie_coefficients import *
get_fourier_coefficients(f,2,2)
get_fourier_coefficients_complex(f, 2, 2)

#3.график f_n

from fourie_plot import *
plot_fourier_series()

#4.график g_n

from fourier_plot_complex import *
plot_fourier_series_complex()

#равенство парсеваля - не написано еще

#задание 2
#1.построим наш график

from complex_function_graph import *
plot_complex_function()

#2.параметрический график суммы фурье

from param_graph import *
plot_fourier_series_parametric()


from fourier_complex_num2 import *
#3.график реальной части + фурье коэффициент
plot_real_part()

#4.график мнимой части + фурье коэффициент
plot_imaginary_part()

#5. парсеваль - не написан




import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Определение функций
def beta1(s):
    return 0.2 * (1 + s) * s

def beta2(s):
    return 0.02 * (1 + s) * s**2

def beta3(s):
    return 0.001333 * (1 + s) * s**3

def f(x):
    return 1 - x

# Вычисление коэффициентов f_i
f1, _ = quad(lambda s: beta1(s) * f(s), 0, 1)
f2, _ = quad(lambda s: beta2(s) * f(s), 0, 1)
f3, _ = quad(lambda s: beta3(s) * f(s), 0, 1)

# Вычисление элементов матрицы A
A11, _ = quad(lambda s: 0.2 * (1 + s) * s**2, 0, 1)
A12, _ = quad(lambda s: 0.2 * (1 + s) * s**3, 0, 1)
A13, _ = quad(lambda s: 0.2 * (1 + s) * s**4, 0, 1)
A21, _ = quad(lambda s: 0.02 * (1 + s) * s**3, 0, 1)
A22, _ = quad(lambda s: 0.02 * (1 + s) * s**4, 0, 1)
A23, _ = quad(lambda s: 0.02 * (1 + s) * s**5, 0, 1)
A31, _ = quad(lambda s: 0.001333 * (1 + s) * s**4, 0, 1)
A32, _ = quad(lambda s: 0.001333 * (1 + s) * s**5, 0, 1)
A33, _ = quad(lambda s: 0.001333 * (1 + s) * s**6, 0, 1)

# Матрица коэффициентов
A = np.array([[1 - A11, -A12, -A13],
              [-A21, 1 - A22, -A23],
              [-A31, -A32, 1 - A33]])

# Вектор правой части
F = np.array([f1, f2, f3])

# Решение системы
C = np.linalg.solve(A, F)

# Приближённое решение
def u_approx(x, n):
    if n == 1:
        return 1 - x + C[0]*x
    elif n == 2:
        return 1 - x + C[0]*x + C[1]*x**2
    elif n == 3:
        return 1 - x + C[0]*x + C[1]*x**2 + C[2]*x**3

# Создание сетки для x
x_values = np.linspace(0, 1, 100)

# Вычисление эталонного решения (n = 3)
u_exact_values = [u_approx(x, 3) for x in x_values]

# Вычисление погрешности для n = 1 и n = 2
error_n1 = [abs(u_approx(x, 1) - u_exact) for x, u_exact in zip(x_values, u_exact_values)]
error_n2 = [abs(u_approx(x, 2) - u_exact) for x, u_exact in zip(x_values, u_exact_values)]

# Построение графика погрешности
plt.plot(x_values, error_n1, label='Погрешность для n=1')
plt.xlabel('x')
plt.ylabel('Погрешность')
plt.legend()
plt.title('График погрешности приближённого решения')
plt.grid(True)
plt.show()
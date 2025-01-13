import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D

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
def u_approx(x):
    return 1 - x + C[0]*x + C[1]*x**2 + C[2]*x**3

# Создание сетки для x и количества членов аппроксимации
x_values = np.linspace(0, 1, 100)
n_values = np.arange(1, 4)  # Количество членов аппроксимации

# Создание сетки для 3D графика
X, N = np.meshgrid(x_values, n_values)
U = np.zeros_like(X)

for i, n in enumerate(n_values):
    for j, x in enumerate(x_values):
        if n == 1:
            U[i, j] = 1 - x + C[0]*x
        elif n == 2:
            U[i, j] = 1 - x + C[0]*x + C[1]*x**2
        elif n == 3:
            U[i, j] = 1 - x + C[0]*x + C[1]*x**2 + C[2]*x**3

# Построение 3D графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, N, U, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('Количество членов аппроксимации')
ax.set_zlabel('u(x)')
ax.set_title('Трёхмерный график приближённого решения')

plt.show()
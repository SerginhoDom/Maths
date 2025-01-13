import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize

# Определение дифференциального уравнения и граничных условий
def differential_equation(u, x):
    return np.gradient(np.gradient(u, x), x) + (2 / (x - 2)) * np.gradient(u, x) + u * (x - 2) - 1

# Точное решение
def exact_solution(x):
    return 1 / (x - 2)

# Метод сплайн-коллокации
def spline_collocation(n):
    x = np.linspace(0, 1, n)
    y = np.zeros(n)
    
    # Начальное приближение
    y[0] = -0.5
    y[-1] = -1
    
    # Минимизация невязки
    def residual(y_interior):
        y_full = np.concatenate(([-0.5], y_interior, [-1]))
        return np.sum(differential_equation(y_full, x)**2)
    
    res = minimize(residual, np.zeros(n-2))
    y_interior = res.x
    y_full = np.concatenate(([-0.5], y_interior, [-1]))
    
    return x, y_full

# Количество узлов
n = 10
x, y_approx = spline_collocation(n)
y_exact = exact_solution(x)

# Построение сплайна
cs = CubicSpline(x, y_approx)

# Таблица сравнения точного и приближённого решения
print("Таблица сравнения точного и приближённого решения:")
print("x\tПриближённое решение\tТочное решение\tПогрешность")
for i in range(len(x)):
    print(f"{x[i]:.2f}\t{y_approx[i]:.6f}\t\t{y_exact[i]:.6f}\t\t{abs(y_approx[i] - y_exact[i]):.6f}")

# График погрешности
plt.figure()
plt.plot(x, abs(y_approx - y_exact), 'r-', label='Погрешность')
plt.xlabel('x')
plt.ylabel('Погрешность')
plt.title('График погрешности')
plt.legend()
plt.grid()

# График сплайна и точного решения
x_plot = np.linspace(0, 1, 100)
plt.figure()
plt.plot(x_plot, cs(x_plot), 'b-', label='Приближённое решение (сплайн)')
plt.plot(x_plot, exact_solution(x_plot), 'g--', label='Точное решение')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Сравнение точного и приближённого решения')
plt.legend()
plt.grid()

plt.show()
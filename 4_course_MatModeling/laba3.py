import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline
from scipy.optimize import minimize

# Определение дифференциального уравнения
def differential_equation(u, x):
    return np.gradient(np.gradient(u, x), x) + (2 / (x - 2)) * np.gradient(u, x) + u * (x - 2) - 1

# Точное решение
def exact_solution(x):
    return 1 / (x - 2)

# Метод сплайн-коллокации с использованием B-сплайнов
def b_spline_collocation(n, k=3):
    # Узлы коллокации
    x_collocation = np.linspace(0, 1, n)
    
    # Узлы для B-сплайна (k+1 дополнительных узлов на каждом конце)
    t = np.linspace(0, 1, n + k + 1)
    
    # Начальное приближение для коэффициентов B-сплайна
    c = np.zeros(n + k)
    
    # Граничные условия
    def boundary_conditions(c):
        spline = BSpline(t, c, k)
        return [spline(0) + 0.5, spline(1) + 1]  # u(0) = -0.5, u(1) = -1
    
    # Функция для минимизации (невязка в узлах коллокации)
    def residual(c):
        spline = BSpline(t, c, k)
        u = spline(x_collocation)
        res = differential_equation(u, x_collocation)
        return np.sum(res**2)
    
    # Минимизация невязки с учётом граничных условий
    constraints = {'type': 'eq', 'fun': boundary_conditions}
    res = minimize(residual, c, constraints=constraints)
    c_opt = res.x
    
    # Оптимальный сплайн
    spline = BSpline(t, c_opt, k)
    
    return x_collocation, spline

# Количество узлов коллокации и степень B-сплайна
n = 10
k = 3
x, spline = b_spline_collocation(n, k)
y_approx = spline(x)
y_exact = exact_solution(x)

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

# График B-сплайна и точного решения
x_plot = np.linspace(0, 1, 100)
plt.figure()
plt.plot(x_plot, spline(x_plot), 'b-', label='Приближённое решение (B-сплайн)')
plt.plot(x_plot, exact_solution(x_plot), 'g--', label='Точное решение')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Сравнение точного и приближённого решения')
plt.legend()
plt.grid()

plt.show()
import numpy as np
import matplotlib.pyplot as plt


# Заданные параметры
a, b = 0, 2  # Интервал
y0 = 1  # Начальное условие
h = 0.1  # Шаг

def f(x, y):
    return 1 / np.cos(x) - y * np.tan(x)

def solutionF(a, b, y0, h):
    x_values = np.arange(a, b+h, h)
    y_values = np.zeros(len(x_values))
    for i in range(0, len(x_values)):
        y_values[i] = np.cos(x_values[i]) + np.sin(x_values[i])
    return y_values

# Метод Эйлера
def euler_method(f, a, b, y0, h):
    x_values = np.arange(a, b + h, h)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0
    for i in range(1, len(x_values)):
        y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])
    return x_values, y_values

# Улучшенный метод Эйлера (метод точек трапеций)
def improved_euler_method(f, a, b, y0, h):
    x_values = np.arange(a, b + h, h)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0
    for i in range(1, len(x_values)):
        k1 = f(x_values[i-1], y_values[i-1])
        k2 = f(x_values[i-1] + h, y_values[i-1] + h * k1)
        y_values[i] = y_values[i-1] + (h / 2) * (k1 + k2)
    return x_values, y_values

# Метод Рунге-Кутта 4-го порядка
def runge_kutta_4(f, a, b, y0, h):
    x_values = np.arange(a, b + h, h)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0
    for i in range(1, len(x_values)):
        k1 = h * f(x_values[i-1], y_values[i-1])
        k2 = h * f(x_values[i-1] + h / 2, y_values[i-1] + k1 / 2)
        k3 = h * f(x_values[i-1] + h / 2, y_values[i-1] + k2 / 2)
        k4 = h * f(x_values[i-1] + h, y_values[i-1] + k3)
        y_values[i] = y_values[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x_values, y_values

# Решения
y_solution = solutionF(a, b, y0, h)
x_euler, y_euler = euler_method(f, a, b, y0, h)
x_improved_euler, y_improved_euler = improved_euler_method(f, a, b, y0, h)
x_rk4, y_rk4 = runge_kutta_4(f, a, b, y0, h)


# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x_euler, y_euler, label="Метод Эйлера")
plt.plot(x_improved_euler, y_improved_euler, label="Улучшенный метод Эйлера")
plt.plot(x_rk4, y_rk4, label="Метод Рунге-Кутта 4-го порядка")
plt.plot(x_euler, y_solution, label="Solution")
plt.title("Решение задачи Коши численными методами")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

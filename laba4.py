import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
l1, l2 = 1.0, 1.0
T = 1.0
N1, N2 = 10, 10
h1, h2 = l1 / N1, l2 / N2
tau = 0.05

# Сетка
x1 = np.linspace(0, l1, N1+1)
x2 = np.linspace(0, l2, N2+1)
t = np.arange(0, T + tau, tau)

# Начальное условие (ненулевое)
v = np.zeros((len(t), N1+1, N2+1))
for i in range(N1+1):
    for j in range(N2+1):
        v[0, i, j] = np.sin(np.pi * x1[i]) * np.sin(np.pi * x2[j])  # Пример начального условия

# Источниковый член φ^n (ненулевой)
def phi(x1, x2, t):
    return np.sin(np.pi * x1) * np.sin(np.pi * x2) * np.exp(-t)  # Пример источникового члена

# Метод расщепления
for n in range(len(t) - 1):
    # Первый этап
    v_half = np.zeros((N1+1, N2+1))
    for i in range(1, N1):
        for j in range(1, N2):
            v_half[i, j] = (v[n, i, j] + 0.5 * tau * (
                (v[n, i+1, j] - 2*v[n, i, j] + v[n, i-1, j]) / h1**2 +
                2 * (v[n, i, j+1] - 2*v[n, i, j] + v[n, i, j-1]) / h2**2 +
                phi(x1[i], x2[j], t[n])  # Добавляем источниковый член
            )) / (1 - 0.5 * tau / h1**2)
    
    # Второй этап
    for i in range(1, N1):
        for j in range(1, N2):
            v[n+1, i, j] = v_half[i, j] + tau * (
                (v_half[i, j+1] - 2*v_half[i, j] + v_half[i, j-1]) / h2**2
            )

# Вывод результатов
for n in range(len(t)):
    print(f"t = {t[n]:.2f}")
    print(v[n])

# График решения
plt.figure()
plt.contourf(x1, x2, v[-1].T, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Приближённое решение')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
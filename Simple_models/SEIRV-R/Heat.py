import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Задаем параметры модели
a = 1.0
alpha = 1.0
v = np.array([1.0, 0.0])
b = 1.0
kappa_a = 1.0
gamma = 1.0
beta = 1.0
Theta_0 = 1.0

# Размеры сетки и области
Nx, Ny = 50, 50
Lx, Ly = 1.0, 1.0
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1)
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Начальные условия
theta = np.ones((Ny, Nx)) * Theta_0
phi = np.ones((Ny, Nx)) * Theta_0 ** 4

# Параметры итерационного процесса
dt = 0.01
iterations = 200


# Функция для обновления значений на каждом шаге
def update(theta, phi):
    theta_new = np.copy(theta)
    phi_new = np.copy(phi)

    for i in range(1, Ny - 1):
        for j in range(1, Nx - 1):
            dtheta_dx = (theta[i, j + 1] - theta[i, j - 1]) / (2 * dx)
            dtheta_dy = (theta[i + 1, j] - theta[i - 1, j]) / (2 * dy)
            d2theta_dx2 = (theta[i, j + 1] - 2 * theta[i, j] + theta[i, j - 1]) / dx ** 2
            d2theta_dy2 = (theta[i + 1, j] - 2 * theta[i, j] + theta[i - 1, j]) / dy ** 2
            d2phi_dx2 = (phi[i, j + 1] - 2 * phi[i, j] + phi[i, j - 1]) / dx ** 2
            d2phi_dy2 = (phi[i + 1, j] - 2 * phi[i, j] + phi[i - 1, j]) / dy ** 2

            theta_new[i, j] = theta[i, j] + dt * (
                    a * (d2theta_dx2 + d2theta_dy2)
                    - v[0] * dtheta_dx - v[1] * dtheta_dy
                    - b * kappa_a * np.abs(theta[i, j]) * theta[i, j] ** 3
                    + b * kappa_a * phi[i, j]
            )

            phi_new[i, j] = phi[i, j] + dt * (
                    alpha * (d2phi_dx2 + d2phi_dy2)
                    - kappa_a * phi[i, j]
                    + kappa_a * np.abs(theta[i, j]) * theta[i, j] ** 3
            )

    # Граничные условия
    theta_new[:, 0] = theta_new[:, 1]  # левая граница
    theta_new[:, -1] = theta_new[:, -2]  # правая граница
    theta_new[0, :] = theta_new[1, :]  # нижняя граница
    theta_new[-1, :] = theta_new[-2, :]  # верхняя граница

    phi_new[:, 0] = phi_new[:, 1]  # левая граница
    phi_new[:, -1] = phi_new[:, -2]  # правая граница
    phi_new[0, :] = phi_new[1, :]  # нижняя граница
    phi_new[-1, :] = phi_new[-2, :]  # верхняя граница

    return theta_new, phi_new


# Настройка графика
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
c1 = ax[0].contourf(X, Y, theta, levels=20, cmap='viridis')
c2 = ax[1].contourf(X, Y, phi, levels=20, cmap='plasma')
fig.colorbar(c1, ax=ax[0])
fig.colorbar(c2, ax=ax[1])
ax[0].set_title('Temperature θ')
ax[1].set_title('Radiative intensity φ')


# Функция анимации
def animate(frame):
    global theta, phi
    theta, phi = update(theta, phi)
    ax[0].clear()
    ax[1].clear()
    c1 = ax[0].contourf(X, Y, theta, levels=20, cmap='viridis')
    c2 = ax[1].contourf(X, Y, phi, levels=20, cmap='plasma')
    fig.colorbar(c1, ax=ax[0])
    fig.colorbar(c2, ax=ax[1])
    ax[0].set_title('Temperature θ')
    ax[1].set_title('Radiative intensity φ')
    ax[0].set_xlim(0, Lx)
    ax[0].set_ylim(0, Ly)
    ax[1].set_xlim(0, Lx)
    ax[1].set_ylim(0, Ly)


# Создание анимации
ani = FuncAnimation(fig, animate, frames=iterations, interval=50)
plt.show()
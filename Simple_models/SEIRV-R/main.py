import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Параметры модели
beta = 0.3   # Коэффициент передачи инфекции
gamma = 0.1  # Коэффициент выздоровления

# Начальные условия: S0 - восприимчивые, I0 - инфицированные, R0 - выздоровевшие
S0 = 0.9
I0 = 0.1
R0 = 0.0
initial_conditions_SIR = [S0, I0, R0]

# Временной интервал
t = np.linspace(0, 160, 160)

# Определение системы дифференциальных уравнений для модели SIR
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Решение системы уравнений для модели SIR
solution_SIR = odeint(sir_model, initial_conditions_SIR, t, args=(beta, gamma))
S_SIR, I_SIR, R_SIR = solution_SIR.T

# Визуализация результатов модели SIR
plt.figure(figsize=(10, 6))
plt.plot(t, S_SIR, label='Восприимчивые (S)')
plt.plot(t, I_SIR, label='Инфицированные (I)')
plt.plot(t, R_SIR, label='Выздоровевшие (R)')
plt.xlabel('Время')
plt.ylabel('Доля населения')
plt.legend()
plt.title('Модель SIR')
plt.show()

# Параметры модели
beta = 0.3   # Коэффициент передачи инфекции
sigma = 0.2  # Коэффициент перехода из состояния E в I
gamma = 0.1  # Коэффициент выздоровления

# Начальные условия: S0 - восприимчивые, E0 - экспонированные, I0 - инфицированные, R0 - выздоровевшие
S0 = 0.9
E0 = 0.1
I0 = 0.0
R0 = 0.0
initial_conditions_SEIR = [S0, E0, I0, R0]

# Определение системы дифференциальных уравнений для модели SEIR
def seir_model(y, t, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

# Решение системы уравнений для модели SEIR
solution_SEIR = odeint(seir_model, initial_conditions_SEIR, t, args=(beta, sigma, gamma))
S_SEIR, E_SEIR, I_SEIR, R_SEIR = solution_SEIR.T

# Визуализация результатов модели SEIR
plt.figure(figsize=(10, 6))
plt.plot(t, S_SEIR, label='Восприимчивые (S)')
plt.plot(t, E_SEIR, label='Экспонированные (E)')
plt.plot(t, I_SEIR, label='Инфицированные (I)')
plt.plot(t, R_SEIR, label='Выздоровевшие (R)')
plt.xlabel('Время')
plt.ylabel('Доля населения')
plt.legend()
plt.title('Модель SEIR')
plt.show()

# Параметры модели
beta = 0.3    # Коэффициент передачи инфекции
sigma = 0.2   # Коэффициент перехода из состояния E в I
gamma = 0.1   # Коэффициент выздоровления
nu = 0.05     # Коэффициент вакцинации
delta = 0.01  # Коэффициент рецидива
mu = 0.01     # Коэффициент рождаемости и смертности

# Начальные условия: S0 - восприимчивые, E0 - экспонированные, I0 - инфицированные, R0 - выздоровевшие, V0 - вакцинированные
S0 = 0.5
E0 = 0.0
I0 = 0.5
R0 = 0.0
V0 = 0.0
initial_conditions_SEIRVR = [S0, E0, I0, R0, V0]

# Определение системы дифференциальных уравнений для модели SEIRV-R
def seirvr_model(y, t, beta, sigma, gamma, nu, delta, mu):
    S, E, I, R, V = y
    N = S + E + I + R + V
    dSdt = mu * N - beta * S * I - nu * S - mu * S + delta * R
    dEdt = beta * S * I - sigma * E - mu * E
    dIdt = sigma * E - gamma * I - mu * I
    dRdt = gamma * I - delta * R - mu * R
    dVdt = nu * S - mu * V
    return [dSdt, dEdt, dIdt, dRdt, dVdt]

# Решение системы уравнений для модели SEIRV-R
solution_SEIRVR = odeint(seirvr_model, initial_conditions_SEIRVR, t, args=(beta, sigma, gamma, nu, delta, mu))
S_SEIRVR, E_SEIRVR, I_SEIRVR, R_SEIRVR, V_SEIRVR = solution_SEIRVR.T

# Визуализация результатов модели SEIRV-R
plt.figure(figsize=(10, 6))
plt.plot(t, S_SEIRVR, label='Восприимчивые (S)')
plt.plot(t, E_SEIRVR, label='Экспонированные (E)')
plt.plot(t, I_SEIRVR, label='Инфицированные (I)')
plt.plot(t, R_SEIRVR, label='Выздоровевшие (R)')
plt.plot(t, V_SEIRVR, label='Вакцинированные (V)')
plt.xlabel('Время')
plt.ylabel('Доля населения')
plt.legend()
plt.title('Модель SEIRV-R')
plt.show()
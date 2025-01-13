import numpy as np
from scipy import linalg

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    step = 0
    phi = initial_guess[:]
    residual = linalg.norm(A @ phi - b)  # Initial residual
    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i, j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
        residual = linalg.norm(A @ phi - b)
        step += 1
        print("Step {} Residual: {:10.6g}".format(step, residual))
    return phi

# An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-4
omega = 0.5  # Relaxation factor

A = np.array([[4, -1, -6, 0],
              [-5, -4, 10, 8],
              [0, 9, 4, -2],
              [1, 0, -7, 5]])

b = np.array([2, 21, -12, -6])

initial_guess = np.zeros(4)
x =  np.linalg.solve(A, b)
phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print("Vector X found from relaxation method: ")
for i in range(len(phi)):
    if i == 0:
        print("[", round(phi[i], 10))
    if i == 3:
        print(round(phi[i], 10), "]")
    if i>0 and i<3:
        print(round(phi[i], 10))
print("Accurate x: ")
for i in range(len(x)):
    if i == 0:
        print("[", round(x[i], 10))
    if i == 3:
        print(round(x[i], 10), "]")
    if i>0 and i<3:
        print(round(x[i], 10))
print("Погрешность:")
for i in range(len(x)):
    if i == 0:
        print("[", round(abs(phi-x)[i], 10))
    if i == 3:
        print(round(abs(phi-x)[i], 10), "]")
    if i>0 and i<3:
        print(round(abs(phi-x)[i], 10))
# print(abs(abs(phi-x)))
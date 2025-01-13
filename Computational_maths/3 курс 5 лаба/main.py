import numpy as np


def simple_iteration(A, b, max_iterations=1000, tolerance=10**(-4)):
    n = len(A)
    x_new = np.array([
        [0],
        [0],
        [0]
    ], dtype=np.longdouble)
    iterations = 0
    a1 = np.zeros((3, 3))

    for i in range(n):
        for j in range(n):
            if i == j:
                b[i] = b[i] / A[i][i]
            else:
                a1[i][j] = (-1 * A[i][j]) / A[i][i]
        a1[i][i] = 0
        print(a1)
        print(b)

    print(x_new, '--------------')
    while iterations < max_iterations:

        if np.linalg.norm((a1 @ x_new + b) - x_new) <= tolerance:
            break
        print('==============================')
        print(b)
        print(x_new)
        print(a1)
        print(a1 @ x_new)
        print(np.linalg.norm((a1 * x_new + b) - x_new))
        print('==============================')
        x_new = a1 @ x_new + b
        print(x_new, '\n')
        iterations += 1

    return x_new, iterations


A = np.array([
    [10, -1, 1],
    [1, 10, -3],
    [1, -2, 10]
])
b = np.array([
    [10],
    [8],
    [9]
], float)

x_exact = np.linalg.solve(A, b)
x, iterations = simple_iteration(A, b)

print("Matrix A:")
print(A)

print("Iterations:")
print(iterations)

print("Vector X founded from simple iteration method:")
print(x)

print("Accurate x:")
print(x_exact)
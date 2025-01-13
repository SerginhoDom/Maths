import numpy as np
from numpy.linalg import norm
import time


def qr_decomposition(matrix):
    rows, cols = matrix.shape
    u = np.zeros((rows, cols))
    r = np.zeros((cols, cols))
    q = np.zeros((rows, cols))
    u[:, 0] = matrix[:, 0]
    q[:, 0] = matrix[:, 0] / norm(matrix[:, 0], 2)

    for i in range(1, rows):
        _sum = 0
        for j in range(0, i):
            _sum += np.dot(matrix[:, i], q[:, j]) * q[:, j]
        u[:, i] = matrix[:, i] - _sum
        q[:, i] = u[:, i] / norm(u[:, i], 2)

    for i in range(rows):
        for j in range(i, cols):
            r[i, j] = np.dot(q[:, i], matrix[:, j])

    return q, r, u


A = np.array([
    [6.03, 13, -17],
    [13, 29.03, -38],
    [-17, -38, 50.03]])
b = np.array([
    [2.0909],
    [4.1509],
    [-5.1191]])
accurateX = np.array([
    [1.03],
    [1.03],
    [1.03]])

Q, R, U = qr_decomposition(A)

y = Q.T.dot(b)
x = np.linalg.solve(R, y)

print("Matrix A:")
print(A)

print("Matrix A:")
print(Q@R)

print("Vector X:")
print(x)

print("\nMatrix Q:")
print(Q)

print("\nMatrix R:")
print(R)

print("\nMatrix U:")
print(U)

start_time = time.time()

A_inv = np.linalg.inv(R) @ np.linalg.inv(Q)
print("\nMatrix A inerted:")
print(A_inv)

end_time = time.time()
print("\nВремя выполнения: ", end_time - start_time, "секунд")

start_time = time.time()

A_inv = np.linalg.inv(A)
print("\nMatrix A 3 inerted:")
print(A_inv)

end_time = time.time()
print("\nВремя выполнения: ", end_time - start_time, "секунд")

matrix = np.random.randint(0, 100, (10, 10))
Q, R, U = qr_decomposition(matrix)

start_time = time.time()

A_inv = np.linalg.inv(R) @ np.linalg.inv(Q)

end_time = time.time()


print("\nMatrix A 10 inerted:")
print(A_inv)

print("\nВремя выполнения: ", end_time - start_time, "секунд")

matrix = np.random.randint(0, 100, (500, 500))
Q, R, U = qr_decomposition(matrix)

start_time = time.time()

A_inv = np.linalg.inv(R) @ np.linalg.inv(Q)

end_time = time.time()


print("\nMatrix A 100 inerted:")
print(A_inv)

print("\nВремя выполнения: ", end_time - start_time, "секунд")
import numpy as np


def sqrt_decomposition(matrix):
    rows, cols = matrix.shape
    U = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(i, cols):
            if i == j:
                sum_val = matrix[i, j] - np.sum(U[:i, i]**2)
                U[i, i] = np.sqrt(np.maximum(sum_val, 0))
            else:
                sum_val = matrix[i, j] - np.sum(U[:i, i] * U[:i, j])
                U[i, j] = sum_val / U[i, i]

    L = U.transpose()
    return L, U


A = np.array([
    [81, -45, 45],
    [-45, 50, -15],
    [45, -15, 38]
])
b = np.array([
    [531],
    [-460],
    [193]
])
accurateX = np.array ([
    [6],
    [-5],
    [-4]
])


A2 = np.array([
    [5.8, 0.3, -0.2],
    [0.3, 4.0, 0.7],
    [-0.2, -0.7, 6.7]
])
b2 = np.array([
    [3.1],
    [-1.7],
    [1.1]
 ])


A3 = np.array([
    [4.12, 0.42, 1.34, 0.88],
    [0.42, 3.95, 1.87, 0.43],
    [1.34, 1.87, 3.20, 0.31],
    [0.88, 0.43, 0.31, 5.17]
])
b3 = np.array([
    [11.17],
    [0.115],
    [9.909],
    [9.349]
])


L, U = sqrt_decomposition(A)

y = np.linalg.matrix_power(L, -1).dot(b)
x = np.linalg.matrix_power(U, -1).dot(y)


print("Matrix A:")
print(A)

print("Vector X:")
print(x)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

L, U = sqrt_decomposition(A2)

y = np.linalg.matrix_power(L, -1).dot(b2)
x = np.linalg.matrix_power(U, -1).dot(y)


print("Matrix A:")
print(A2)

print("Vector X:")
print(x)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

L, U = sqrt_decomposition(A3)

y = np.linalg.matrix_power(L, -1).dot(b3)
x = np.linalg.matrix_power(U, -1).dot(y)


print("Matrix A:")
print(A3)

print("Vector X:")
print(x)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)





import numpy as np

# исходная матрица
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# QR-разложение
Q, R = np.linalg.qr(A)

print('\n', Q, '\n', R, '\n')

# столбец b
b = np.array([1, 0, 0])

# решение системы уравнений
x = np.linalg.solve(R, np.dot(Q.T, b))

print(Q)
print(x)
# обратная матрица
A_inv = np.dot(np.linalg.inv(Q), np.linalg.inv(R))

print('asca \n', A_inv)
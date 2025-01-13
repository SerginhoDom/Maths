import numpy as np


def jacobi_rotation(A, tol=1e-10, max_iter=1000):

    n = len(A)
    eigenvectors = np.eye(n)  # Начальные собственные векторы - единичная матрица
    iterations = 0

    while True:
        # Находим максимальный недиагональный элемент
        off_diag_indices = np.triu_indices(n, k=1)
        max_off_diag_index = np.argmax(np.abs(A[off_diag_indices]))
        i, j = off_diag_indices[0][max_off_diag_index], off_diag_indices[1][max_off_diag_index]

        # Проверяем условие остановки
        if np.abs(A[i, j]) < tol or iterations >= max_iter:
            break

        # Вычисляем угол поворота
        theta = 0.5 * np.arctan2(2 * A[i, j], A[i, i] - A[j, j])

        # Строим матрицу вращения
        rotation_matrix = np.eye(n)
        rotation_matrix[i, i] = rotation_matrix[j, j] = np.cos(theta)
        rotation_matrix[i, j] = -np.sin(theta)
        rotation_matrix[j, i] = np.sin(theta)

        # Применяем вращение к матрице и собственным векторам
        A = np.dot(np.dot(rotation_matrix.T, A), rotation_matrix)
        eigenvectors = np.dot(eigenvectors, rotation_matrix)

        iterations += 1

    eigenvalues = np.diag(A)

    return eigenvalues, eigenvectors, iterations


matrix1 = np.array([[4, -2, 2, -1],
                    [-2, 2, -4, 1],
                    [2, -4, 3, -2],
                    [-1, 1, -2, 3]])
matrix2 = np.array([[4, -2, 2, -1, -1],
                    [-2, 2, -4, 1, -1],
                    [2, -4, 3, -2, 2],
                    [-1, 1, -2, 3, -2],
                    [-1, -1, 2, -2, 4]])
matrix3 = np.array([[4, -2, 2, -1, -1, 2, 3],
                    [-2, 2, -4, 1, -1, 2, 3],
                    [2, -4, 3, -2, 2, 2, 3],
                    [-1, 1, -2, 3, -2, 2, 3],
                    [-1, -1, 2, -2, 4, 2, 3],
                    [2, 2, 2, 2, 2, 2, 3],
                    [3, 3, 3, 3, 3, 3, 3],])

eigenvalues, eigenvectors, iterations = jacobi_rotation(matrix1)
print("Собственные значения:", eigenvalues)
print("Собственные векторы: \n", eigenvectors)
print("Количество итераций: ", iterations)

eigenvalues, eigenvectors, iterations = jacobi_rotation(matrix2)
print("Собственные значения:", eigenvalues)
print("Собственные векторы: \n", eigenvectors)
print("Количество итераций: ", iterations)

eigenvalues, eigenvectors, iterations = jacobi_rotation(matrix3)
print("Собственные значения:", eigenvalues)
print("Собственные векторы: \n", eigenvectors)
print("Количество итераций: ", iterations)
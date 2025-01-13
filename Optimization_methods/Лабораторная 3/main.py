import numpy as np


def find_corner_solution(simplex_matrix):
    i = 0
    solution = np.zeros(6)

    for j in range (0, 6):
        if simplex_matrix[0][j] == 0:
            while simplex_matrix [i][j] == 0:
                i += 1
                solution[j] = simplex_matrix[i][14]
    return solution


def find_final_matrix(double_matrix, b):
    simplex_matrix = np.zeros((7, 15))
    simplex_matrix[:, :14] = double_matrix[:, :14]
    simplex_matrix[0, :8] = b
    simplex_matrix[:, 14] = double_matrix[:, 20]

    return simplex_matrix

def find_dual_corner_solution(simplex_matrix):
    i = 0
    solution = np.zeros(14)
    sum = 0
    k = 0

    for j in range (0, 14):
        sum = 0
        for i in range (0, 7):
            sum += simplex_matrix[i][j]
        if sum == 1:
            for i in range(0, 7):
                if simplex_matrix[i][j] != 0:
                    solution[j] = simplex_matrix[i][20]

    return solution


def find_final_corner_solution(simplex_matrix):
    i = 0
    solution = np.zeros(8)
    sum = 0
    k = 0

    for j in range (0, 8):
        sum = 0
        for i in range (0, 7):
            sum += simplex_matrix[i][j]
        if sum == 1:
            for i in range(0, 7):
                if simplex_matrix[i][j] != 0:
                    solution[j] = simplex_matrix[i][14]

    return solution


def create_simplex_matrix(a, b, c):

    simplex_matrix = np.zeros((9, 15))
    print(simplex_matrix)
    simplex_matrix[0, :6] = np.copy(c) * (-1)
    simplex_matrix[1:9, :6] = np.copy(a)
    simplex_matrix[1:9, 14] = np.copy(b)
    simplex_matrix[1:9, 6:14] = np.eye(8)
    print(simplex_matrix)

    return simplex_matrix


def create_double_task_matrix(A, c):
    AT = A.transpose()
    result_matrix = np.zeros((AT.shape[0] + 1, AT.shape[1] + AT.shape[0] * 2 + 1), np.double)

    for i in range(AT.shape[0]):
        result_matrix[i + 1, -1] = c[0, i]

    for i in range(AT.shape[0]):
        for j in range(AT.shape[1]):
            result_matrix[i + 1, j] = AT[i, j]

    I = np.eye(AT.shape[0])
    I *= -1

    for i in range(AT.shape[0]):
        for j in range(AT.shape[0]):
            result_matrix[i + 1, j + AT.shape[1]] = I[i, j]

    I *= -1
    for i in range(AT.shape[0]):
        for j in range(AT.shape[0]):
            result_matrix[i + 1, j + AT.shape[1] + AT.shape[0]] = I[i, j]
    for i in range(AT.shape[0]):
        result_matrix[0, i + AT.shape[1] + AT.shape[0]] = 1
    for i in range (1, 7):
        result_matrix[0, :21] -= result_matrix[i, :21]
    return result_matrix


def find_key_element(simplex_matrix):
    local_min = 0
    column_number = 0
    row_number = 0

    for j in range(0, 15):
        if (simplex_matrix[0][j] < 0) and (abs(simplex_matrix[0][j]) > local_min):
            local_min = np.copy(abs(simplex_matrix[0][j]))
            column_number = j

    local_min = 0

    for i in range(1, 9):
        if simplex_matrix[i][column_number]/simplex_matrix[i][14] > local_min:
            local_min = simplex_matrix[i][column_number]/simplex_matrix[i][14]
            row_number = i

    print('Номер строки = ', row_number, '\n', 'Номер столбца = ', column_number, '\n')
    return simplex_matrix[row_number][column_number], row_number, column_number


def find_final_key_element(simplex_matrix):
    local_min = 0
    column_number = 0
    row_number = 0

    for j in range(0, 15):
        if (simplex_matrix[0][j] < 0) and (abs(simplex_matrix[0][j]) > local_min):
            local_min = np.copy(abs(simplex_matrix[0][j]))
            column_number = j

    local_min = 0

    for i in range(1, 7):
        if simplex_matrix[i][column_number]/simplex_matrix[i][14] > local_min:
            local_min = simplex_matrix[i][column_number]/simplex_matrix[i][14]
            row_number = i

    print('Номер строки = ', row_number, '\n', 'Номер столбца = ', column_number, '\n')
    return simplex_matrix[row_number][column_number], row_number, column_number


def find_key_element_double_task(simplex_matrix):
    local_min = 0
    column_number = 0
    row_number = 0

    for j in range(0, 20):
        if (simplex_matrix[0][j] < 0) and (abs(simplex_matrix[0][j]) > local_min):
            local_min = np.copy(abs(simplex_matrix[0][j]))
            column_number = j

    local_min = 0

    for i in range(1, 7):
        if simplex_matrix[i][column_number]/simplex_matrix[i][20] > local_min:
            local_min = simplex_matrix[i][column_number]/simplex_matrix[i][20]
            row_number = i

    print('\n Номер строки = ', row_number, '\n', 'Номер столбца = ', column_number, '\n')
    return simplex_matrix[row_number][column_number], row_number, column_number


def simplex(a, b, c):

    simplex_matrix = create_simplex_matrix(a, b, c)
    flag = 1
    x = np.zeros(6)
    iterations = 0

    while flag == 1:
        flag = 0
        iterations += 1

        permissive_element, permissive_row, permissive_column = find_key_element(simplex_matrix)
        print('Разрешающий элемент = ', permissive_element, ' \n')
        for j in range(0, 15):
            simplex_matrix[permissive_row][j] = simplex_matrix[permissive_row][j] / permissive_element

        for i in range(0, 9):
            buf = np.copy(simplex_matrix[i][permissive_column])
            if i != permissive_row:
                for j in range(0, 15):
                    simplex_matrix[i][j] -= simplex_matrix[permissive_row][j] * buf

        for j in range (0, 15):
            if simplex_matrix[0][j] < 0:
                flag = 1
        for i in range(0, 9):
            print('\n')
            for j in range(0, 15):
                print(round(simplex_matrix[i][j], 1), ' ', end='')

    x = find_corner_solution(simplex_matrix)
    return x, iterations

def simplex_double_task(a, b, c):

    simplex_matrix = create_double_task_matrix(a, c)
    print(simplex_matrix)
    flag = 1
    x = np.zeros(14)
    iterations = 0

    while flag == 1:
        flag = 0
        iterations += 1

        permissive_element, permissive_row, permissive_column = find_key_element_double_task(simplex_matrix)
        print('Разрешающий элемент = ', permissive_element, ' \n')
        for j in range(0, 21):
            simplex_matrix[permissive_row][j] = simplex_matrix[permissive_row][j] / permissive_element

        for i in range(0, 7):
            buf = np.copy(simplex_matrix[i][permissive_column])
            if i != permissive_row:
                for j in range(0, 21):
                    simplex_matrix[i][j] -= simplex_matrix[permissive_row][j] * buf

        for j in range (0, 21):
            if simplex_matrix[0][j] < 0:
                flag = 1
            if iterations == 17:
                flag = 0
        for i in range(0, 7):
            print('\n')
            for j in range(0, 21):
                print(round(simplex_matrix[i][j], 1), ' ', end='')

    x = find_dual_corner_solution(simplex_matrix)
    return x, iterations, simplex_matrix


def final_simplex(a, b):

    simplex_matrix = find_final_matrix(a, b)
    simplex_matrix[0][:] = simplex_matrix[0][:] - 6 * simplex_matrix[5][:]
    flag = 1
    x = np.zeros(6)
    iterations = 0

    while flag == 1:
        flag = 0
        iterations += 1

        permissive_element, permissive_row, permissive_column = find_final_key_element(simplex_matrix)
        print('Разрешающий элемент = ', permissive_element, ' \n')
        for j in range(0, 15):
            simplex_matrix[permissive_row][j] = simplex_matrix[permissive_row][j] / permissive_element

        for i in range(0, 7):
            buf = np.copy(simplex_matrix[i][permissive_column])
            if i != permissive_row:
                for j in range(0, 15):
                    simplex_matrix[i][j] -= simplex_matrix[permissive_row][j] * buf

        for j in range (0, 15):
            if simplex_matrix[0][j] < 0:
                flag = 1
            if iterations == 2:
                flag = 0
        for i in range(0, 7):
            print('\n')
            for j in range(0, 15):
                print(round(simplex_matrix[i][j], 1), ' ', end='')

    x = find_final_corner_solution(simplex_matrix)
    return x, iterations


A = np.array([[15, 47, 55, 10, 25, 60],
       [55, 39, 93, 67, 42, 16],
       [81, 61, 10, 77, 96, 89],
       [91, 61, 38, 22, 77, 52],
       [14, 92, 62, 49, 17, 73],
       [95, 43, 66, 95, 56, 56],
       [37, 33, 28, 31, 62, 51],
       [52, 76, 81, 37, 99, 27]], dtype=np.longdouble)
b = np.array([[6, 16, 10, 15, 12, 6, 15, 3]], dtype=np.longdouble)

c = np.array([[21, 59, 51, 84, 89, 10]], dtype=np.longdouble)


x, iterations = simplex(A, b, c)
print(x, iterations)
double_matrix = create_double_task_matrix(A, c)
print(double_matrix)
x, iterations, double_matrix = simplex_double_task(A, b, c)
print(x, iterations)
final_matrix = find_final_matrix(double_matrix, b)
for i in range(0, 7):
    print('\n')
    for j in range(0, 15):
        print(round(final_matrix[i][j], 1), ' ', end='')
final_matrix[0][:] = final_matrix[0][:] - 6 * final_matrix[5][:]
print ('\n-------------------------------------------------------------------------------', )
for i in range(0, 7):
    print('\n')
    for j in range(0, 15):
        print(round(final_matrix[i][j], 1), ' ', end='')

x, iterations = final_simplex(double_matrix, b)
print(x, iterations)

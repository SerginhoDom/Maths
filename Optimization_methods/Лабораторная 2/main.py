import numpy as np
from numpy.linalg import norm


def function(x, A, b):
    f = 1/2 * x.transpose() * A * x + b * x
    return f


def lagrange(x, A, b, y, x0, r):

    L = 1/2 * x.transpose() * A * x + b * x + y * (norm(x - x0, ord = 1) - r**2)
    dL = A * x + b + 2 * y * (x - x0)
    return L, dL


def Newton(x,A, b, y, x0, r):

    epsilon = 10**(-6)
    identityMatrix = np.eye(4)
    LagrangeDerivative = np.zeros((5, 1))
    jacobiMatrix = np.zeros((5, 5))
    buf = np.zeros((5, 1))
    buf[:4, :] = np.copy(x0)
    buf[4] = y

    print(LagrangeDerivative, '\n', A, '\n', identityMatrix, '\n', x, '\n', b, '\n', y, '\n', identityMatrix, '\n', x0, '\n')
    print(np.dot((A + 2 * identityMatrix * y), x))
    LagrangeDerivative[:4, :] = (A + 2 * identityMatrix * y) @ x[:4, :] + (b + 2 * y * x0)
    LagrangeDerivative[4] = np.linalg.norm(x - x0) ** 2 - r ** 2

    jacobiMatrix[:4, :4] = A + 2 * identityMatrix * y
    jacobiMatrix[:4, 4] = 2 * (x - x0)[:4, 0]
    jacobiMatrix[4, :4] = 2 * (x - x0)[:4, 0].transpose()

    buf2 = np.zeros((5, 1))
    buf2[:4, :] = np.copy(x0)
    buf2[4] = np.copy(y)
    new_x = buf2[:5, :] - np.linalg.inv(jacobiMatrix) @ LagrangeDerivative[:5, :]
    print(jacobiMatrix, '\n', LagrangeDerivative, '\n', buf2)

    while np.linalg.norm(new_x - buf) > epsilon:

        buf = np.copy(new_x)
        # Преобразованная производная функции Лагранжа
        LagrangeDerivative[:4, :] = (A + 2 * identityMatrix * y) @ new_x[:4, :] + (b + 2 * y * x0)
        LagrangeDerivative[4] = np.linalg.norm(new_x[:4, :] - x0) ** 2 - r ** 2

        jacobiMatrix[:4, :4] = A + 2 * identityMatrix * y
        jacobiMatrix[:4, 4] = 2 * (new_x[:4, :] - x0)[:4, 0]
        jacobiMatrix[4, :4] = 2 * (new_x[:4, :] - x0)[:4, 0].transpose()

        new_x = buf[:5, :] - np.linalg.inv(jacobiMatrix) @ LagrangeDerivative[:5, :]
        y = new_x[4, 0]
        print(np.linalg.norm(new_x - buf))

    return new_x[:4, :]


A = np.array([
    [-0.298439, -0.488296, -0.503806, 1.03377],
    [-0.488296,   0.127771,   0.468747,  -0.850776],
    [-0.503806,   0.468747,  -0.202294,  -0.357976],
    [1.03377,  -0.850776,  -0.357976,  -0.312017]
])
b = np.array([[-0.184819], [0.336055], [0.531485], [-0.384315]])
x0 = np.array([[0.207971], [1.02182], [0.0609925], [0.498329]])
r = 7  # радиус сферы (произвольное число)
y = r

x1 = np.copy(x0)
x1[1] = x0[1] - r
print(x1, '\n')
x2 = np.copy(x0)
x2[1] = x0[1] + r
print(x2, '\n')
x3 = np.copy(x0)
x3[2] = x0[2] - r
print(x3, '\n')
x4 = np.copy(x0)
x4[2] = x0[2] + r
print(x4, '\n')
x5 = np.copy(x0)
x5[3] = x0[3] - r
print(x5, '\n')
x6 = np.copy(x0)
x6[3] = x0[3] + r
print(x6, '\n')
x7 = np.copy(x0)
x7[0] = x0[0] - r
print(x7, '\n')
x8 = np.copy(x0)
x8[0] = x0[0] + r
print(x8, '\n')

g = Newton(x1, A, b, y, x0, r)

print('Предположим, y = 0. Тогда имеем:\n')
ApplicantX1 = -1 * np.linalg.matrix_power(A, -1) * b

print(np.linalg.norm(ApplicantX1 - x0), '<>', r)

if np.linalg.norm(ApplicantX1 - x0) <= r:
    print('Точка', ApplicantX1, 'Подходит и будет рассматриваться в будущем\n')
else:
    print('Точка', ApplicantX1, 'Не подходит и не будет рассматриваться в будущем\n')

print('Функция от икса = ', g)




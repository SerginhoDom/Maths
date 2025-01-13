import numpy as np
import pprint as pp
from math import *
import copy
import pandas as pd


def CreateMatrixForStraightTask(A, b, c):
  rowsAndColumns = A.shape
  rowsResultMatrix = rowsAndColumns[0] + 1
  columnsResultMatrix =  rowsAndColumns[0] + rowsAndColumns[1] + 1
  resultMatrix = np.zeros((rowsAndColumns[0] + 1, rowsAndColumns[0] + rowsAndColumns[1] + 1))

  for i in range(rowsAndColumns[1]):
    resultMatrix[0, i] = -1 * c[0, i]

  for i in range(rowsAndColumns[0]):
    resultMatrix[i+ 1, -1] = b[i, 0]

  for i in range(rowsAndColumns[0]):
    for j in range(rowsAndColumns[1]):
      resultMatrix[i + 1, j] = A[i, j]

  I = np.eye(rowsAndColumns[0])
  for i in range(rowsAndColumns[0]):
    for j in range(rowsAndColumns[0]):
      resultMatrix[i + 1, j + rowsAndColumns[1]] = I[i, j]

  return resultMatrix


def getCCoordinate(A, CSize, minC):
  for i in range(CSize):
    if A[0, i] == minC :
      return i


def FindResolvingRow(A, resolvingColumn, BSize):
  m = 0
  resolvingRow = 0
  for i in range(1, BSize + 1):
    temp = A[i, -1] / A[i, resolvingColumn]
    if temp > 0:
      m = temp
      resolvingRow = i
      break

  if (m == 0 and resolvingRow == 0):
    return -1

  for i in range(2, BSize + 1):
    temp = A[i, -1] / A[i, resolvingColumn]
    if temp < abs(m) and temp > 0:
      m = temp
      resolvingRow = i

  return resolvingRow


def SubtractResolvingRow(A, resolvingColumn, resolvingRow):
  derevativ = copy.copy(A[resolvingRow, resolvingColumn])
  for i in range(A.shape[1]):
    A[resolvingRow, i] /= derevativ

  for j in range(A.shape[0]):

    if j == resolvingRow:
      continue

    factor = copy.copy(A[j, resolvingColumn])
    for i in range(A.shape[1]):
      A[j, i] -= factor * A[resolvingRow, i]


def FindMaxResult(A, CSize, BSize, name):
  minC = np.min(A[0, :CSize])
  np.savetxt(name + str(0) + '.csv', A, delimiter=',', fmt='%s')
  i = 1
  print(minC)
  while minC < 0:
    resolvingColumn = getCCoordinate(A, CSize, minC)
    resolvingRow = FindResolvingRow(A, resolvingColumn, BSize)
    print("_____________________________")
    print("iteration num = " + str(i))
    print("reolving row = " + str(resolvingRow))
    print("reolving column = " + str(resolvingColumn))
    print("resolving element = " + str(A[resolvingRow, resolvingColumn]))

    SubtractResolvingRow(A, resolvingColumn, resolvingRow)
    np.set_printoptions(precision=1)
    np.set_printoptions(suppress = True)
    print(bmatrix(A))


    print(*A, sep='\n')
    print("_____________________________")
    i += 1
    minC = min(A[0, :CSize])


def CheckForAuxiliaryTask(list):
  for i in range(0, len(list)):
    if round(list[i], 12) != 0 or (list[i] < 0):
      return False
  return True


def AuxiliaryTask(A, CSize, BSize):
  minC = min(A[0, :CSize])
  np.savetxt('doubleTask' + str(0) + '.csv', A, delimiter=',', fmt='%s')
  k = 1
  while CheckForAuxiliaryTask(A[0, :-(BSize + 1)]) == False:
    #for i in range(A.shape[0]):
      #for j in range(A.shape[1]):
        #A[i, j] = round(A[i, j], 16)

    resolvingColumn = getCCoordinate(A, CSize, minC)
    resolvingRow = FindResolvingRow(A, resolvingColumn, BSize)
    print("_____________________________")
    print("iteration num = " + str(k))
    print("reolving row = " + str(resolvingRow))
    print("reolving column = " + str(resolvingColumn))
    print("resolving element = " + str(A[resolvingRow, resolvingColumn]))
    if (resolvingColumn == -1 or resolvingRow == -1):
      return

    SubtractResolvingRow(A, resolvingColumn, resolvingRow)
    print(bmatrix(A))

    np.set_printoptions(suppress = True)
    print(*A, sep='\n')
    np.savetxt('Laba-4_doubleTask' + str(k) + '.csv', A, delimiter=',', fmt='%.1f')
    print("_____________________________")
    k += 1
    minC = min(A[0, :CSize])


def bmatrix(a, precision = 1):
    text = r'\left('
    text += r'\matrix{'
    for x in range(len(a)):
        for y in range(len(a[x])):
            text += str(round(a[x][y], ndigits=precision))
            text += r' & '
        text = text[:-2]
        text += r'\\'
    text += r'}'
    text += r'\right)'

    return text


def PrintMatrix(matrix):
  for row in matrix:
    print (' '.join(map(str, row)))


def FindSolution(A):
  result = []
  for i in range(A.shape[1] - 1):
    sum = 0
    index = 0
    for j in range(1, A.shape[0]):
      if A[j, i] == 1:
        index = j
      sum += A[j, i]

    if sum == 1:
      result.append(A[index, -1])
    else:
      result.append(0)
  return np.array([result])


def CreateMatrixForDoubleTask(A, с):
  AT = A.transpose()
  resultMatrix = np.zeros((AT.shape[0] + 1, AT.shape[1] + AT.shape[0] * 2 + 1), np.double)

  for i in range(AT.shape[0]):
    resultMatrix[i + 1, -1] = c[0, i]

  for i in range(AT.shape[0]):
    for j in range(AT.shape[1]):
      resultMatrix[i + 1, j] = AT[i, j]

  I = np.eye(AT.shape[0])
  I *= -1

  for i in range(AT.shape[0]):
    for j in range(AT.shape[0]):
      resultMatrix[i + 1, j + AT.shape[1]] = I[i, j]

  I *= -1
  for i in range(AT.shape[0]):
    for j in range(AT.shape[0]):
      resultMatrix[i + 1, j + AT.shape[1] + AT.shape[0]] = I[i, j]
  for i in range(AT.shape[0]):
    resultMatrix[0, i + AT.shape[1] + AT.shape[0]] = 1
  return resultMatrix


def TranslateMatrixToStraightTask(A):
  for i in range(1, A.shape[0]):
    for j in range(A.shape[1]):
      A[0, j] -= A[i, j]


def ConvertMatrixToSecondStraightInDoubleTask(A, b):
  resultMatrix = np.zeros((A.shape[0], A.shape[1] - A.shape[0] + 1))
  for i in range(resultMatrix.shape[0]):
    for j in range(resultMatrix.shape[1] - 1):
      resultMatrix[i, j] = A[i, j]

  for i in range(1, resultMatrix.shape[0]):
    resultMatrix[i, -1] = A[i, -1]

  for j in range(b.shape[0]):
    resultMatrix[0, j] = b[j, 0]

  return resultMatrix


def SustractRowFromZeroRow(A, row, column):
  factor = copy.copy(A[0, column])
  for i in range(A.shape[1]):
    A[0, i] = A[0, i] - A[row, i]*factor


def SelectBasicColumns(A, len):
  for i in range(len):
    sum = 0
    for j in range(1, A.shape[0]):
      sum += A[j, i]
    if (sum == 1):
      for j in range(1, A.shape[0]):
        if A[j, i] == 1:
          SustractRowFromZeroRow(A, j, i)


def FindDouwnGamePrice(A):
    minElementInColumns = []
    for i in range(A.shape[0]):
        minElementInColumns.append(min(A[i]))

    douwnGamePrice = max(minElementInColumns)
    return douwnGamePrice


def FindUpGamePrice(A):
    maxElementsInRows = []
    for j in range(A.shape[1]):
        maxElementsInRows.append(max(A[:, j]))

    upGamePrice = min(maxElementsInRows)
    return upGamePrice


def AddElementForEveryElement(A, element):
    new_A = np.copy(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            new_A[i, j] += element

    return new_A


A= np.array([[-10,  -2,  -2,   4,   2,   5,   5,   4],
       [ -1,   6,  -8,  -4,  -2,   5,  -8,   4],
       [  2,   8,  -7,   4,   7,  -1,  -8,   8],
       [ -4,   9,   5,   6,   4,   5,  -4,  -5],
       [ -3,  -2,   1,   4,  -9,   9, -10,   0],
       [  3,  -3,  -2,  -2,  -2,  -9,  -2,  -5]])

downGamePrice = FindDouwnGamePrice(A)
print(downGamePrice)

upGamePrice = FindUpGamePrice(A)
print(upGamePrice)

minElement = np.min(A)
print(minElement)
NonNegativA = AddElementForEveryElement(A, abs(minElement))
print(bmatrix(NonNegativA))

print('Создание матрицы для прямой задачиЫ')
b = np.array([[1, 1, 1, 1, 1, 1]])
c = np.array([[1, 1, 1, 1, 1, 1, 1, 1]])
straightMatrix = CreateMatrixForStraightTask(NonNegativA, b.transpose(), c)
print(bmatrix(straightMatrix))

print('Решение прямой задачи')
FindMaxResult(straightMatrix, 14, 6, 'laba-4_straight')
print(straightMatrix)

print('Угловое решение:')
solution = FindSolution(straightMatrix)
np.set_printoptions(precision=3)
np.set_printoptions(suppress = True)
print(bmatrix(solution, 3))

print('Значение целевой функции')
print(straightMatrix[0, -1])

print('Оптимальная стратегий второго игрока')
optimalStrategySecondPlayer = solution / np.linalg.norm(solution)
print(bmatrix(optimalStrategySecondPlayer, 3))

print('Создание матрицы для дввойтвенной задачи')
doubleTaskMatrix = CreateMatrixForDoubleTask(NonNegativA, np.array([[1, 1, 1, 1, 1, 1, 1, 1]]))
print(doubleTaskMatrix)
np.savetxt('Laba-4_doubleTaskMatrix.csv', doubleTaskMatrix, delimiter=',', fmt='%s')

print('Выделение базисных столбцов')
TranslateMatrixToStraightTask(doubleTaskMatrix)
print(doubleTaskMatrix)
np.savetxt('Laba-4_doubleTask0.csv', doubleTaskMatrix, delimiter=',', fmt='%s')

print('Решение вспомогательной задачи')
AuxiliaryTask(doubleTaskMatrix, 15, 8)

print('Угловое решение')
np.set_printoptions(precision=3)
np.set_printoptions(suppress = True)
print(bmatrix(solution, 3))

print('Приведение матрицы для решения двойственной задачи')
secondDoubleTaskMatrix = ConvertMatrixToSecondStraightInDoubleTask(doubleTaskMatrix, np.array([[1], [1], [1], [1], [1], [1]]))
print(bmatrix(secondDoubleTaskMatrix))

print('Выделение базисных столлбцов')
np.savetxt('Laba-4_before_BasicColumn.csv', secondDoubleTaskMatrix, delimiter=',', fmt='%s')
SelectBasicColumns(secondDoubleTaskMatrix, A.shape[0])
np.savetxt('basicColumn_Laba4.csv', secondDoubleTaskMatrix, delimiter=',', fmt='%s')
print(bmatrix(secondDoubleTaskMatrix))

FindMaxResult(secondDoubleTaskMatrix, secondDoubleTaskMatrix.shape[1] - 1, secondDoubleTaskMatrix.shape[0] - 1, 'Laba-4_doubleTaskStraight')

print('Оптимальная стратегия игрока 1')
np.set_printoptions(precision=3)
np.set_printoptions(suppress = True)
solution = FindSolution(secondDoubleTaskMatrix)
print(bmatrix(solution, 3))
print(np.linalg.norm(solution))
print(bmatrix(solution / np.linalg.norm(solution), 3))


print('Значение целевой функции:')
print(secondDoubleTaskMatrix[0, -1])

print('Конечные ответы:')
print ((1 / -secondDoubleTaskMatrix[0, -1]) + minElement)
print(downGamePrice)
print(upGamePrice)
print(bmatrix(solution / np.linalg.norm(solution), 3))
print(bmatrix(optimalStrategySecondPlayer, 3))

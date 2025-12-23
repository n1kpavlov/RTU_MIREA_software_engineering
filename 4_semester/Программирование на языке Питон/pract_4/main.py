#1
print("#1")
def smalldet(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

A = [[4, 3],
     [1, 1]]

determinant = smalldet(A)
print("Определитель матрицы A:", determinant)


#2
print("\n#2")
def submatrix(A, i, j):
    return [row[:j] + row[j+1:] for row_idx, row in enumerate(A) if row_idx != i]

A = [
    [0, 2, 1],
    [1, 4, 3],
    [2, 1, 1]
]

print("submatrix(A, 0, 0):", submatrix(A, 0, 0))
print("submatrix(A, 1, 1):", submatrix(A, 1, 1))
print("submatrix(A, 2, 1):", submatrix(A, 2, 1))


#3
print("\n#3")
def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return smalldet(A)

    determinant = 0
    i = 0
    for j in range(n):
        sub = submatrix(A, i, j)
        sign = (-1) ** (i + j)
        determinant += sign * A[i][j] * det(sub)

    return determinant

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

determinant = det(A)
print("Определитель матрицы A:", determinant)


#4
print("\n#4")
def minor(A, i, j):
    sub = submatrix(A, i, j)
    return det(sub)

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

minor_value = minor(A, 0, 1)
print("Дополнительный минор элемента a,0,1:", minor_value)


#5
print("\n#5")
def alg(A, i, j):
    return (-1) ** (i + j) * minor(A, i, j)

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

alg_value = alg(A, 1, 1)
print("Алгебраическое дополнение элемента a,1,1:", alg_value)


#6
print("\n#6")
def algmatrix(A):
    n = len(A)
    return [[alg(A, i, j) for j in range(n)] for i in range(n)]

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

alg_mat = algmatrix(A)
print("Матрица алгебраических дополнений:")
for row in alg_mat:
    print(row)


#7
print("\n#7")
def inverse_matrix(A):
    n = len(A)
    det_A = det(A)
    if det_A == 0:
        raise ValueError("Матрица вырожденная, обратной матрицы не существует.")

    alg_mat = algmatrix(A)
    adjugate = [[alg_mat[j][i] for j in range(n)] for i in range(n)]
    inverse = [[adjugate[i][j] / det_A for j in range(n)] for i in range(n)]
    return inverse

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

inverse_A = inverse_matrix(A)
print("Обратная матрица:")
for row in inverse_A:
    print(row)


#8
print("\n#8")
def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*B)] for row_A in A]

def more_penrose(H):
    H_T = transpose_matrix(H)
    H_T_H = matrix_multiply(H_T, H)
    H_T_H_inv = inverse_matrix(H_T_H)
    H_plus = matrix_multiply(H_T_H_inv, H_T)
    return H_plus

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

A_plus = more_penrose(A)
print("Псевдообращение Мура-Пенроуза для матрицы A:")
for row in A_plus:
    print(row)
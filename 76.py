import random

N = 5  # �����
M = 7  # ��������

K = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i &lt; len(matrix):
        j = 0
        row = matrix[i]
        while j &lt; len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


def get_column(matrix, index):
    column = []
    i = 0
    while i &lt; len(matrix):
        column.append(matrix[i][index])
        i += 1

    return column


A = get_matrix(N, M)
print("�������� �������:")
print_matrix(A)

k_column = get_column(A, K - 1)

i = 0
while i &lt; len(A):
    j = 0

    while j &lt; len(A[i]):
        A[i][j] *= k_column[i]
        j += 1

    i += 1

print("��������������� �������:")
print_matrix(A)

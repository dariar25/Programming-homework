import random

N = 5  # �����
M = 7  # ��������

L = 3
K = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))

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


A = get_matrix(N, M)
print("�������� �������:")
print_matrix(A)

l_zeros = 0
k_zeros = 0


i = 0
while i &lt; len(A):
    j = 0

    while j &lt; len(A[i]):
        if A[i][j] == 0:
            if i &lt; L:
                l_zeros += 1

            if j &lt; K:
                k_

zeros += 1
        j += 1

    i += 1

print("� ������� %s ������� ���������� %s �����" % (L, l_zeros))
print("� ����� %s �������� ���������� %s �����" % (K, k_zeros))

import random

N = 2  # �����
M = 3  # ��������


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

new_row = []

i = 0
while i &lt; len(A):
    j = 0

    count_row_negative = 0
    while j &lt; len(A[i]):
        is_negative = A[i][j] &lt; 0

        if is_negative:
            count_row_negative += 1

        if len(new_row) &lt;= j:
            new_row.append(1 if is_negative else 0)
        else:
            new_row[j] += 1 if is_negative else 0

        j += 1

    A[i].append(count_row_negative)
    i += 1

A.append(new_row)

print("���������������� �������:")
print_matrix(A)

import random

N = 2  # �����
M = 3  # ��������


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
        while j &lt; len(row): column = row[j] print(column, end=' ') j += 1 print() i += 1 def get_average(row): sum = 0 for element in row: sum += element return sum/len(row) A = get_matrix(N, M) print("�������:") print_matrix(A) n = 0 for row in A: average = get_average(row) if average &gt; n:
        n = average


print("���������� �������� ����� ������� �������� ��� ������ ������ "
      "�������:", n)

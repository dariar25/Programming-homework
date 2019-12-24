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


def listsum(list):
    sum = 0
    for element in list:
        sum += element

    return sum


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

tmp = list(zip(*A))

max_sum = 0
index_column_max_sum = 0

i = 0
while i &lt; len(tmp): column = tmp[i] current_list_sum = listsum(column) if current_list_sum &gt; max_sum:
        max_sum = current_list_sum
        index_column_max_sum = i

    i += 1

print("�������:")
print_matrix(A)
print("C������ ��� �������� ����� ���������� �������� ��������� �����������:",
      index_column_max_sum)
print("���������� ������� ����� �������:", min(tmp[index_column_max_sum]))

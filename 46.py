import random

N = 11
T = random.randint(0, 100)


def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
count_positive = 0
print("�������� ������:        ", lst)
print("����� T:", T)

for element in lst:
    if element &gt;= 0:
        count_positive += 1

i = 0
while i &lt; len(lst): if lst[i] &gt;= 0:
        lst[i] += T/count_positive

    i += 1

print("���������� ������������� �����:", count_positive)
print("���� ������� ������������ � ������� �� ���:", T/count_positive)
print("������ ����� �����������:", lst)

import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("������:        ", lst)

is_up = True
prev = lst[0]

i = 0
while i &lt; len(lst):
    element = lst[i]

    if element &lt; 0:
        break

    if element &lt; prev:
        is_up = False

    prev = element
    i += 1


if i == 0:
    print("������������������ �� ������ ��������")
elif i == 1:
    print("������������������ ������� �� 1 ��������")
elif is_up:
    print("������������������ ����������")
else:
    print("������������������ �� ����������")

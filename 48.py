import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("�������� ������:        ", lst)


i = 0
while i &lt; len(lst): if lst[i] == 0: if i &gt; 1:
            lst[i] = lst[i-1] + lst[i-2]
        elif i == 1:
            lst[i] = lst[i - 1]
        else:
            print("������ ������� 0, ��� ������ �������� ������ ��� ��� ��������������")

    i += 1

print("������ ����� �����������:", lst)

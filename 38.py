import random
import math

N = 11
M = 3
K = 4

def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(-100, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("�������� ������:        ", lst)

del lst[K:K+M]

print("���������������� ������:", lst)

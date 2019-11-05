import random
import math
def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(7)
print("Source array:", lst)
centre = math.ceil(len(lst) / 2)
lst = lst[centre:] + lst[:centre]

print("Modified array:", lst)

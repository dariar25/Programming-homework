import random
def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(8)
print("Source array:", lst)

val = lst[len(lst) - 1]
for i in range(len(lst)):
    val, lst[i],  = lst[i], val

print("Modified array:", lst)

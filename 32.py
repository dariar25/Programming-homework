import random
def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(9)
print("Source array:", lst)

for i in range(len(lst) - 1):
    if i % 2 == 0:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print("Modified array:", lst)

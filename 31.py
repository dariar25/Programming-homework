import random
def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list

lst = init_random_list(5)
print("Source array:", lst)

i = 0
while i &lt; len(lst): i = i + 1 for j in range(len(lst) - i): if lst[j] &gt; lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Sorted array:", lst)

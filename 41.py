import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size &gt; 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Массив:        ", lst)

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
    print("Последовательность не успела начаться")
elif i == 1:
    print("Последовательность состоит из 1 элемента")
elif is_up:
    print("Последовательность возрастает")
else:
    print("Последовательность не возрастает")

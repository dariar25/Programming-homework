import random

M = random.randint(1,10)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()

print(arr)

print("���������� �������� � ����� ������� ������: " + str(len(max(arr))))

K = len(max(arr))

for i in range(M):
    N = K - len(arr[i])

print("*" * N + str(arr[i]))

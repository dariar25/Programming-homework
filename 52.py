import random
M=random.randint(1,10)
arr=[random.randint(1,10) for i in range(M)]
for i in range (M):
	arr[i]=input()
	print(arr)
	b=arr[0]
	for i in range(1,M):
		b=str(b)+" "+arr[i]
		print(b)

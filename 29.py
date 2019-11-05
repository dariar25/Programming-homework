import random
import math
A = random.randint(0,2020)
print(A)
if A%4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
B = A//100
vek = B+1
print("century-",vek)

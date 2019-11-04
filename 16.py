import random
ch=random.randint (1,9999)
k=ch//500  
k1=ch - 500*k
k2=k1//100  
k3=100*k2
k4=k1-k3
k5=k4-k4//10*10
print(ch)
if ch//500:
  print(str(ch//500), " - po 500")
else:
 print("0  - po 500")
if k1//100:
 print(str(k1//100)," - po 100")
else:
 print("0  - po 100")	
if k4//10:
 print(str(k4//10)," - po 10")
else:
 print("0  - po 10")
if k5//2:
 print(str(k5//2)," - po 2")
else:
 print("0  - po 2")

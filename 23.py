import random
import math

X = random.randint (1,58)
Y = random.randint (1,23)
print ("X - ",X)
print ("Y - ",Y)
if X &gt; Y :
    Z = math.sqrt(X*Y)
    print("Zqrt - ",Z)
else:
    Z = math.log(X+Y)
    print ("Zlog - ",Z)

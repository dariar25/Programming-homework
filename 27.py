import random
import math
X = random.randint(1.0,5.0)
if X&lt;= 0:
    f = 0
    print("f("+str(X)+")="+str(f))
if 0&lt;X&lt;1:
    f = X**2-X
    print ("f("+str(X)+")="+str(f))
else:
    f = X**2-math.sin(math.pi**2)
    print("f("+str(X)+")="+str(f))

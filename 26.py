import random
X = random.randint(1.0,5.0)
if X&lt;= 0 :
    print("f("+str(X)+")="+str(f))
if 0&lt;X&lt;1:
    print("f("+str(X)+")="+str(f))
else:
    f = X**4
    print("f("+str(X)+")="+str(f))

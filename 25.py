import random
X = random.randint(1,5)
if X &lt;= 2 :
    f = X**2 + 4*X + 5
    print("f("+str(X)+")="+ str(f))
else:
    f = 1/(X**2 + 4*X + 5)
    print("f("+str(X)+")="+str(f))

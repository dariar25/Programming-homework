import random
a=random.randint(1,50)
print("a= " + str(a))
b=random.randint(1,50)
print("b= " + str(b))
c=random.randint(1,50)
print("c= " + str(c))
d=random.randint(1,50)
print("d= " + str(d))
if (a &lt;= c and b &lt;= d) or (a &lt;= d and b &lt;= c):
    print("A rectangle with sides a, b will fit in a rectangle with sides c, d")
if not (a &lt;= c and b &lt;= d) or not (a &lt;= d and b &lt;= c):
    print("A rectangle with sides a, b does not fit in a rectangle with sides c, d")

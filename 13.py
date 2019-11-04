import math
D = 8
print("(D) Cross section diameter = " + str(D))
A = 2
print("(A) Width of square beam = " + str(A))
d = A * math.sqrt( 5 )
print("(d) Diagonal beam = " + str(d))
if D &gt;= d :
print("Can")
if D &lt; d :
print("must not")

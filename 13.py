import math
D = 8
print("(D) Диаметр поперечного сечения = " + str(D))
A = 2
print("(A) Ширина квадратного бруса = " + str(A))
d = A * math.sqrt( 5 )
print("(d) Диагональ бруса = " + str(d))
if D &gt;= d :
print("Можно")
if D &lt; d :
print("Нельзя")

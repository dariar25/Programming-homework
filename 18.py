import random
import math
A = random.randint (1,5)
V = A**3
print ("Cube volume",V)
P = math.pi
H = random.randint (1,5)
R = random.randint (1,3)
W = (P*R**2)*H
print ("Cylinder volume",W)
Vg = random.randint (1,50)
print ("Fluid volume",Vg)
if Vg &gt; V :
    print ("Can fill the cube")
else:
    print ("You cannot fill a cube")
if Vg &gt; W :
    print ("Can fill cylinder")
else:
    print("Cannot fill cylinder")
if Vg &gt; V+W :
    print("Can fill two")
else :
    print ("can't fill two")

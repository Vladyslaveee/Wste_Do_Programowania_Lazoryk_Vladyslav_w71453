#lab1.11

import math
from mpmath.math2 import math_sqrt

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = b**2 - 4*c*a
print(d)
if d  == 0:
    print((-b/(2*a)))
elif d>0:
    x1 = ((-b-math.sqrt(d))/(2*a))
    x2 = ((-b+math.sqrt(d))/(2*a))
    print(f"your answer is: x1 = {x1}, x2 =  {x2}")
else:
    print("your task cannot be....")
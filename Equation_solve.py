# import numpy as np
# from sympy import symbols, Eq, solve

# x, y = symbols('x y')
# eq1 = Eq(x + y - 5)
# eq2 = Eq(x - y + 3)
# solve((eq1,eq2), (x, y))

# import sympy as sym
from sympy import *
x,y = symbols('x,y')
eq1 = Eq(x+y,5)
eq2 = Eq(x**2+y**2,17)
result = solve([eq1,eq2],(x,y))
print(result)
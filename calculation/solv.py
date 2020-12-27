"""
##方程式を解く。

x^3 + 2x^2 - 5x - 6 = 0　を解く。

"""
"""
$ pip install sympy
"""


import sympy

x = sympy.Symbol('x')
equation = x**3 + 2 * x**2 - 5 * x - 6

print(sympy.solve(equation, x))
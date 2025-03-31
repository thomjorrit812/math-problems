import sympy

# Define symbols
x, y = sympy.symbols('x y')

# Solve equation: x^2 + 3xy - y^2 = 0
solution = sympy.solve(x**2 + 3*x*y - y**2, (x, y))

print(solution)

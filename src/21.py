import numpy as np
from scipy.optimize import minimize

def f(x):
    return x[0]**2 + 3*x[1] - 4

result = minimize(f, [1, 1])
print(result.x)

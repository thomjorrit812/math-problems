import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x):
    return -x**2 + 4*x + 3

result = minimize(f, x0=1)
print("Optimized value:", result.fun)

x_opt = result.x[0]
y_opt = -x_opt**2 + 4*x_opt + 3
plt.scatter(x, y, color='green')
plt.plot([0, 5], [0, 5])
plt.show()

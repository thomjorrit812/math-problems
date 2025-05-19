import numpy as np
import sympy

def calculate_sine_pi():
    # Generate values for pi
    pi_values = np.linspace(0, 2*np.pi, 100)
    
    # Calculate sine and pi for each value
    sine_values = np.sin(pi_values)
    pi_values = pi_values - np.pi/4
    
    # Print the results
    print("Sine values:", sine_values)
    print("Pi values:", pi_values)

calculate_sine_pi()

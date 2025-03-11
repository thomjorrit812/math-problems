
from random import randint

def get_random_math_problem():
    # Generate two random numbers
    num1 = randint(1, 10)
    num2 = randint(1, 10)

    # Choose a random operator (+, -, *, /)
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    # Return the math problem as a string
    return f'{num1} {operator} {num2}'
import random

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Get a random operation (+, -, *, /)
    op = random.choice(['+', '-', '*', '/'])

    # Return the problem in the format (num1, op, num2)
    return (num1, op, num2)

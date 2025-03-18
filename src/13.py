import random
def random_math_problem(a, b):
    operand = random.choice(['+', '-', '*'])
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    else:
        return a * b
import random

def get_random_math_problem(max_value):
    op = random.choice(['+', '-', '*', '/'])
    num1 = random.randint(0, max_value)
    num2 = random.randint(0, max_value)
    if op == '+':
        return f"{num1} + {num2}"
    elif op == '-':
        return f"{num1} - {num2}"
    elif op == '*':
        return f"{num1} * {num2}"
    else:
        return f"{num1} / {num2}"

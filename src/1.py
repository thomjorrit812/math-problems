import random

def get_random_math_problem(operators=("+", "-")):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(operators)
    if operator == "+":
        return f"{num1} + {num2}"
    else:
        return f"{num1} - {num2}"
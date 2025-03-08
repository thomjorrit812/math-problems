import random

def generate_random_math_problem(difficulty):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    operands = ['+', '-', '*', '/']
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    op = random.choice(operands)
    if difficulty == "easy":
        return f"{num1} {op} {num2} = ?"
    elif difficulty == "medium":
        return f"({num1} {op} {num2}) + ({num1} {op} {num2}) = ?"
    else:
        return f"({num1} {op} {num2}) * ({num1} {op} {num2}) = ?"

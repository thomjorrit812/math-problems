import random

def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    operation = random.choice(["+", "-", "*", "/"])
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    problem_text = f"What is {num1} {operation} {num2}?"
    solution = eval(problem_text)
    return problem_text, solution

def get_random_math_problem():
    # Generate a random number between 1 and 10
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    # Generate a random operator (+, -, *, /)
    op = choice(["+", "-", "*", "/"])
    problem = f"{num1} {op} {num2}"
    return problem

def get_random_math_problem(max_number=10):
    """
    Returns a tuple of two numbers that can be added or subtracted together to form a math problem.
    The range of the numbers is determined by the max_number parameter.
    """
    number1 = random.randint(1, max_number)
    number2 = random.randint(1, max_number)
    if random.random() < 0.5:
        return (number1, "+", number2)
    else:
        return (number1, "-", number2)

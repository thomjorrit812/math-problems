 import random
 
def get_random_math_problem(numbers):
    operator = ['+', '-', '*', '/']
    problem = f'{random.choice(numbers)}{operator[1]}{random.choice(numbers)}={}'
    return problem
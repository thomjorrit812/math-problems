import random

def generate_math_problem():
    # Generate a random number between 1 and 50
    num = random.randint(1, 50)
    
    if num % 2 == 0:
        problem = f"Find the sum of all even numbers from 1 to {num}"
        answer = "The sum is: "
    else:
        problem = f"Find the product of all odd numbers from 1 to {num}"
        answer = "The product is: "
    
    return (problem, answer)

generate_math_problem()

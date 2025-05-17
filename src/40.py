import math

def calculate_sum(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

numbers = [10, 20, 30]
result = calculate_sum(numbers)
print(result)

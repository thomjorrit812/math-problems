def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
    return total

n = 5
result = sum_of_squares(n)
print(f"The sum of squares up to {n} is: {result}")

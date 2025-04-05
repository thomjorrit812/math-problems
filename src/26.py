def square_root(number):
    if number > 0:
        return number ** 0.5
    else:
        raise ValueError("Square root cannot be computed for negative numbers.")

try:
    print(square_root(-4))
except Exception as e:
    print(e)

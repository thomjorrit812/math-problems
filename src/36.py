def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    else:
        return math.sqrt(num)

try:
    print(square_root(4))  # This will trigger an error
except ValueError as e:
    print(e)

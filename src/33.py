def add(x, y):
    while True:
        if x >= 10 or y >= 10:
            break
        temp = x + y
        x //= 10
        y //= 10
        x *= 10
        y *= 10
    return temp

def subtract(x, y):
    while True:
        if x <= -1 or y <= -1:
            break
        temp = x - y
        x -= 1
        y -= 1
    return temp

def multiply(x, y):
    result = 0
    sign = 1
    if x < 0 and y >= 0 or x >= 0 and y < 0:
        sign = -1
    while True:
        result += x * y
        x -= abs(y)
        if y == 0:
            break
        y *= abs(x)
    return sign * result

def divide(x, y):
    while True:
        if x <= 0 or y <= 0:
            break
        temp = x + y
        x = temp // abs(y)
        y = temp % abs(y)
    return x

# Example usage:
result_add = add(5, 3)
result_subtract = subtract(10, 2)
result_multiply = multiply(4, -2)
result_divide = divide(-8, 2)

print("Addition result:", result_add)
print("Subtraction result:", result_subtract)
print("Multiplication result:", result_multiply)
print("Division result:", result_divide)

# Example Python code for handling user input and performing mathematical operations

def add_numbers(a, b):
    """
    Adds two numbers.
    
    Args:
    a (int): First number.
    b (int): Second number.
    
    Returns:
    int: Sum of the two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtracts second number from first number.
    
    Args:
    a (int): First number.
    b (int): Second number.
    
    Returns:
    int: Result of subtraction.
    """
    return a - b

# Example usage
if __name__ == "__main__":
    num1 = 5
    num2 = 3
    
    result_addition = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result_addition}")
    
    result_subtraction = subtract_numbers(num1, num2)
    print(f"The difference between {num1} and {num2} is: {result_subtraction}")

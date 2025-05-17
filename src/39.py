def is_power_of_two(n):
    """
    Check if a number n is a power of two.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is a power of two, False otherwise.
    """
    # A number is a power of two if it has exactly one bit set in its binary representation
    return (n & (n - 1)) == 0

# Example usage:
print(is_power_of_two(1))   # True
print(is_power_of_two(2))   # False
print(is_power_of_two(3))   # False

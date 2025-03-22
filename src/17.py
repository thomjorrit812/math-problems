import math

def is_power_of_two(n):
    """
    Check if a given positive integer n is a power of two.
    
    :param n: A positive integer to check
    :return: True if n is a power of two, False otherwise
    """
    return n > 0 and (n & (n - 1)) == 0

def sum_of_odd_numbers(numbers):
    """
    Calculate the sum of all odd numbers in a given list.
    
    :param numbers: A list of integers
    :return: The sum of all odd numbers in the list
    """
    return sum(number for number in numbers if number % 2 != 0)

def fibonacci_sequence(length):
    """
    Generate and print a Fibonacci sequence up to length terms.
    
    :param length: An integer indicating the number of terms in the Fibonacci sequence
    """
    series = [0, 1]
    while len(series) < length:
        next_term = series[-1] + series[-2]
        series.append(next_term)
    print(f"The first {length} terms of the Fibonacci sequence are: {series}")

def main():
    # Example usage
    numbers = [i for i in range(10)]
    print("The sum of all odd numbers in the list is:", sum_of_odd_numbers(numbers))
    
    fibonacci_length = 10
    fibonacci_sequence(fibonacci_length)

if __name__ == "__main__":
    main()

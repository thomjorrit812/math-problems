def print_sum_range(start, end):
    sum = 0
    for num in range(start, end + 1):
        sum += num
    print(f"The sum of numbers from {start} to {end} is: {sum}")

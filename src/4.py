  def solve_math_problem(problem):
    """Solves a math problem in the form '1+2' and returns the result as an integer."""
    numbers = [int(i) for i in problem.split('+')]
    return numbers[0] + numbers[1]
# Task 1: Calculate Factorial Using a Function

def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample input
try:
    num = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input! Please enter an integer.")

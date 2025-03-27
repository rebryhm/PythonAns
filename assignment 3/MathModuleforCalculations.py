# Task 2: Using the Math Module for Calculations

import math

try:
    # Taking user input
    num = float(input("Enter a number: "))

    # Calculating required values
    sqrt_value = math.sqrt(num)
    log_value = math.log(num) if num > 0 else "Undefined (logarithm not defined for non-positive numbers)"
    sine_value = math.sin(num)

    # Displaying results
    print(f"Square root of {num}: {sqrt_value}")
    print(f"Natural logarithm of {num}: {log_value}")
    print(f"Sine of {num} (in radians): {sine_value}")

except ValueError:
    print("Invalid input! Please enter a valid number.")

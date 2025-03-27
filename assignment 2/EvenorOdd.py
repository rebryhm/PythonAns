# Task 1: Check if a Number is Even or Odd

# Taking input from the user
try:
    num = int(input("Enter an integer: "))

    # Checking if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

except ValueError:
    print("Invalid input! Please enter an integer.")

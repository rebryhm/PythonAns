# Task 2: Write and Append Data to a File

file_name = "output.txt"

# Writing user input to the file
try:
    with open(file_name, "w") as file:
        user_input = input("Enter text to write to the file: ")
        file.write(user_input + "\n")
    print(f"Data written to {file_name}")

    # Appending additional data
    with open(file_name, "a") as file:
        additional_input = input("Enter additional text to append to the file: ")
        file.write(additional_input + "\n")
    print(f"Additional data appended to {file_name}")

    # Reading and displaying final content
    with open(file_name, "r") as file:
        print("\nFinal file content:")
        print(file.read())

except Exception as e:
    print(f"An error occurred: {e}")


# Task 1: Read a File and Handle Errors

try:
    # Attempt to open and read the file
    with open("sample.txt", "r") as file:
        print("File content:")
        for line in file:
            print(line.strip())  # Strip to remove extra newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist. Please create the file and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 1: Create a Dictionary of Student Marks

# Sample dictionary of students and marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eve": 95
}

# Get user input for student name
student_name = input("Enter the student's name: ")

# Retrieve and display marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Error: Student '{student_name}' not found in the records.")

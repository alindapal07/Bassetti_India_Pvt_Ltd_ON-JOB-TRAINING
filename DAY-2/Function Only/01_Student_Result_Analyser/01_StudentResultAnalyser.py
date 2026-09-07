# Student Result Analyzer
#
# Create a program that accepts multiple students:
#
# students = [
#     {"name": "Tarun", "marks": [80, 72, 91]},
#     {"name": "Ashmita", "marks": [65, 88, 79]},
#     {"name": "Alinda", "marks": [35, 42, 38]},
#     {"name": "Pritam", "marks": [79, 41, 26]},
#     {"name": "Anirban", "marks": [81, 91, 31]}
# ]
#
# Create functions to:
#
# 1. Calculate average marks
# 2. Determine PASS/FAIL
# 3. Find the topper
# 4. Find the lowest-performing student
# 5. Calculate class average
#
# Note:
# - Use only functions.
# - Do not use OOP/classes.
# - Assume a student passes only if they score at least 40
#   in every subject.

students = [
    {"name": "Tarun", "marks": [80, 72, 91]},
    {"name": "Ashmita", "marks": [65, 88, 79]},
    {"name": "Alinda", "marks": [35, 42, 38]},
    {"name": "Pritam", "marks": [79, 41, 26]},
    {"name": "Anirban", "marks": [81, 91, 31]}
]


# 1. Calculate average marks of a student
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


# 2. Determine PASS / FAIL
# Assuming minimum 40 marks in every subject
def check_result(marks):
    for mark in marks:
        if mark < 40:
            return "FAIL"

    return "PASS"


# 3. Find the topper
def find_topper(students):
    topper = students[0]

    for student in students:
        if calculate_average(student["marks"]) > calculate_average(topper["marks"]):
            topper = student

    return topper


# 4. Find the lowest-performing student
def find_lowest_student(students):
    lowest = students[0]

    for student in students:
        if calculate_average(student["marks"]) < calculate_average(lowest["marks"]):
            lowest = student

    return lowest


# 5. Calculate class average
def calculate_class_average(students):
    total = 0

    for student in students:
        total = total + calculate_average(student["marks"])

    class_average = total / len(students)

    return class_average


# Display individual student results
print("----- STUDENT RESULTS -----")

for student in students:
    average = calculate_average(student["marks"])
    result = check_result(student["marks"])

    print("Name    :", student["name"])
    print("Marks   :", student["marks"])
    print("Average :", round(average, 2))
    print("Result  :", result)
    print()


# Find topper
topper = find_topper(students)

print("----- TOPPER -----")
print("Name    :", topper["name"])
print("Average :", round(calculate_average(topper["marks"]), 2))
print()


# Find lowest-performing student
lowest = find_lowest_student(students)

print("----- LOWEST PERFORMER -----")
print("Name    :", lowest["name"])
print("Average :", round(calculate_average(lowest["marks"]), 2))
print()


# Class average
class_average = calculate_class_average(students)

print("----- CLASS AVERAGE -----")
print("Class Average :", round(class_average, 2))
# 1. append()

# Adds one element at the end.
students = ["Tarun", "Alinda", "Pritam"]
students. append("Ashmita")
print(students)
# Output:
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita']


# 2. extend()
# Adds multiple elements to the list.
students = ["Tarun", "Alinda"]
students. extend(["Pritam", "Ashmita", "Anirban"])
print(students)
# Output:
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita', 'Anirban']
 
 
# 3. insert()
# Adds an element at a given index.
students = ["Tarun", "Pritam", "Ashmita"]
students. insert(1, "Alinda")
print(students)
# Output:
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita']

# 4. remove()
# Removes the first matching element.
students = ["Tarun", "Alinda", "Pritam", "Alinda"]
students. remove("Alinda")
print(students)
# Output:
# ['Tarun', 'Pritam', 'Alinda']

# 5. pop()
# Removes and returns an element.
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
student = students. pop()
print(student)
print(students)
# Output:
# Ashmita
# ['Tarun', 'Alinda', 'Pritam']



# pop(index)
# Removes an element from the given index.
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
student = students. pop(1)
print(student)
print(students)

# Output:
# Alinda
# ['Tarun', 'Pritam', 'Ashmita']


# 6. clear()
# Removes all elements.
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
students. clear()
print(students)
# Output:
# []


# 7. index()
# Returns the index of an element.
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
print(students. index("Pritam"))
# Output:
# 2

# index(value, start)
# Searches from the given index.
students = ["Tarun", "Alinda", "Pritam", "Alinda", "Ashmita"]
print(students. index("Alinda", 2))

# Output:
# 3

# index(value, start, stop)
# Searches within a particular range.
students = ["Tarun", "Alinda", "Pritam", "Alinda", "Ashmita"]
print(students. index("Alinda", 2, 4))
# Output:
# 3

# 8. count()
# Counts how many times an element occurs.
students = ["Tarun", "Alinda", "Pritam", "Alinda", "Ashmita"]
print(students. count("Alinda"))
# Output:
# 2

# 9. sort()
# Arranges elements in ascending order.
marks = [78, 92, 65, 88, 70]
marks. sort()
print(marks)
# Output:
# [65, 70, 78, 88, 92]



# sort(reverse=True)
# Arranges elements in descending order.
marks = [78, 92, 65, 88, 70]
marks. sort(reverse=True)
print(marks)

# Output:
# [92, 88, 78, 70, 65]



# sort(key=len)
# Sorts according to length.
students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban", "Subhoraj"]
students. sort(key=len)
print(students)

# Output:
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita', 'Anirban', 'Subhoraj']



# sort(key=len, reverse=True)
# Sorts according to length in descending order.
students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban", "Subhoraj"]
students. sort(key=len, reverse=True)
print(students)
# Output:
# ['Subhoraj', 'Anirban', 'Ashmita', 'Alinda', 'Tarun', 'Pritam']


# sort() with lambda
# Sorts a nested list using one value.
students = [
["Tarun", 78],
["Alinda", 92],
["Pritam", 65],
["Ashmita", 88]
]
students. sort(key=lambda x: x[1])
print(students)
# Output:
# [['Pritam', 65], ['Tarun', 78], ['Ashmita', 88], ['Alinda', 92]]



# 10. reverse()
# Reverses the current order.
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
students. reverse()
print(students)
# Output:
# ['Ashmita', 'Pritam', 'Alinda', 'Tarun']
# 11. copy()
# Creates a copy of the list.
students = ["Tarun", "Alinda", "Pritam"]
new_students = students. copy()
print(new_students)

# Output:
# ['Tarun', 'Alinda', 'Pritam']



# Changing the copied list.

students = ["Tarun", "Alinda", "Pritam"]
new_students = students. copy()
new_students. append("Ashmita")
print(students)
print(new_students)
# Output:
# ['Tarun', 'Alinda', 'Pritam']
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita']


# List indexing
students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban", "Subhoraj"]
print(students[0])
print(students[2])
print(students[-1])
print(students[-2])
# Output:
# Tarun
# Pritam
# Subhoraj
# Anirban

# List slicing
students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban", "Subhoraj"]
print(students[1: 4])
# Output:
# ['Alinda', 'Pritam', 'Ashmita']
print(students[: 3])
# Output:
# ['Tarun', 'Alinda', 'Pritam']
print(students[3: ])
# Output:
# ['Ashmita', 'Anirban', 'Subhoraj']
print(students[:: 2])
# Output:
# ['Tarun', 'Pritam', 'Anirban']
print(students[:: -1])
# Output:
# ['Subhoraj', 'Anirban', 'Ashmita', 'Pritam', 'Alinda', 'Tarun']

# Changing list element
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
students[1] = "Anirban"
print(students)
# Output:
# ['Tarun', 'Anirban', 'Pritam', 'Ashmita']
# Changing multiple elements

students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
students[1: 3] = ["Anirban", "Subhoraj"]
print(students)

# Output:
# ['Tarun', 'Anirban', 'Subhoraj', 'Ashmita']

# Adding elements using slicing

students = ["Tarun", "Alinda", "Ashmita"]
students[1: 2] = ["Pritam", "Anirban", "Subhoraj"]
print(students)
# Output:
# ['Tarun', 'Pritam', 'Anirban', 'Subhoraj', 'Ashmita']

# Removing elements using slicing
students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban"]
students[1: 4] = []
print(students)

# Output:
# ['Tarun', 'Anirban']

# del
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
del students[1]
print(students)
# Output:
# ['Tarun', 'Pritam', 'Ashmita']

# del with slicing
students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban"]
del students[1: 4]
print(students)
# Output:
# ['Tarun', 'Anirban']

# List concatenation
a = ["Tarun", "Alinda"]
b = ["Pritam", "Ashmita"]
print(a + b)

# Output:
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita']

# List repetition
students = ["Tarun", "Alinda"]
print(students * 3)
# Output:
# ['Tarun', 'Alinda', 'Tarun', 'Alinda', 'Tarun', 'Alinda']

# Membership operator
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
print("Pritam" in students)
print("Anirban" in students)
print("Anirban" not in students)

# Output:
# True
# False
# True

# len()
# Returns the number of elements.
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
print(len(students))
# Output:
# 4

# max()
# Returns the biggest value.

marks = [78, 92, 65, 88, 70]
print(max(marks))
# Output:
# 92

# min()
# Returns the smallest value.

marks = [78, 92, 65, 88, 70]
print(min(marks))
# Output:
# 65

# sum()
# Returns the total of the values.
marks = [78, 92, 65, 88, 70]
print(sum(marks))
# Output:
# 393

# sorted()
# Returns a new sorted list.
marks = [78, 92, 65, 88, 70]
new_marks = sorted(marks)
print(marks)
print(new_marks)

# Output:
# [78, 92, 65, 88, 70]
# [65, 70, 78, 88, 92]

# sorted(reverse=True)
# Returns a new list in descending order.

marks = [78, 92, 65, 88, 70]
print(sorted(marks, reverse=True))
# Output:
# [92, 88, 78, 70, 65]

# reversed()
# Returns the elements in reverse order.
students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
new_students = list(reversed(students))
print(new_students)

# Output:
# ['Ashmita', 'Pritam', 'Alinda', 'Tarun']

# Nested list
students = [
["Tarun", 20],
["Alinda", 21],
["Pritam", 22],
["Ashmita", 20]
]

print(students)
print(students[0])
print(students[0][0])
print(students[0][1])
# Output:
# [['Tarun', 20], ['Alinda', 21], ['Pritam', 22], ['Ashmita', 20]]
# ['Tarun', 20]
# Tarun
# 20

# List unpacking
students = ["Tarun", "Alinda", "Pritam"]
a, b, c = students

print(a)
print(b)
print(c)
# Output:
# Tarun
# Alinda
# Pritam
# Extended unpacking

students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban"]
a, *b, c = students

print(a)
print(b)
print(c)

# Output:
# Tarun
# ['Alinda', 'Pritam', 'Ashmita']
# Anirban
# List comprehension
marks = [10, 20, 30, 40, 50]
new_marks = [x * 2 for x in marks]
print(new_marks)
# Output:
# [20, 40, 60, 80, 100]

# List comprehension with condition
marks = [10, 20, 30, 40, 50, 60]
even_marks = [x for x in marks if x % 2 == 0]
print(even_marks)

# Output:
# [10, 20, 30, 40, 50, 60]
# List comprehension with names

students = ["Tarun", "Alinda", "Pritam", "Ashmita"]
new_students = [name. upper() for name in students]
print(new_students)

# Output:
# ['TARUN', 'ALINDA', 'PRITAM', 'ASHMITA']

# List comprehension with condition
students = ["Tarun", "Alinda", "Pritam", "Ashmita", "Anirban", "Subhoraj"]
new_students = [name for name in students if len(name) > 6]
print(new_students)
# Output:
# ['Ashmita', 'Anirban', 'Subhoraj']

# Assignment and copy
a = ["Tarun", "Alinda", "Pritam"]
b = a
b. append("Ashmita")
print(a)
print(b)

# Output:
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita']
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita']


# copy()

a = ["Tarun", "Alinda", "Pritam"]
b = a. copy()
b. append("Ashmita")
print(a)
print(b)

# Output:
# ['Tarun', 'Alinda', 'Pritam']
# ['Tarun', 'Alinda', 'Pritam', 'Ashmita']
# Tuple
students = ("Tarun", "Alinda", "Pritam", "Ashmita", "Anirban", "Subhoraj")
print(students)
# Output:
# ('Tarun', 'Alinda', 'Pritam', 'Ashmita', 'Anirban', 'Subhoraj')


# count()
# Counts how many times a value is present.
students = ("Tarun", "Alinda", "Pritam", "Alinda", "Ashmita")
print(students. count("Alinda"))
# Output:
# 2


# count() when value is not present
students = ("Tarun", "Alinda", "Pritam")
print(students. count("Anirban"))
# Output:
# 0


# index()
# Returns the position of a value.
students = ("Tarun", "Alinda", "Pritam", "Ashmita")
print(students. index("Pritam"))
# Output:
# 2


# index() with duplicate values
students = ("Tarun", "Alinda", "Pritam", "Alinda", "Ashmita")
print(students. index("Alinda"))
# Output:
# 1


# index() with start
students = ("Tarun", "Alinda", "Pritam", "Alinda", "Ashmita")
print(students. index("Alinda", 2))
# Output:
# 3


# len()
# Returns the number of elements.
students = ("Tarun", "Alinda", "Pritam", "Ashmita")
print(len(students))
# Output:
# 4



# max()
# Returns the biggest value.
marks = (78, 92, 65, 88, 70)
print(max(marks))
# Output:
# 92



# min()
# Returns the smallest value.
marks = (78, 92, 65, 88, 70)
print(min(marks))
# Output:
# 65



# sum()
# Returns the total of the values.
marks = (78, 92, 65, 88, 70)
print(sum(marks))
# Output:
# 393



# Membership operator
students = ("Tarun", "Alinda", "Pritam", "Ashmita")
print("Pritam" in students)
# Output:
# True
print("Anirban" in students)
# Output:
# False
# not in
students = ("Tarun", "Alinda", "Pritam", "Ashmita")
print("Anirban" not in students)
# Output:
# True



# Indexing
students = ("Tarun", "Alinda", "Pritam", "Ashmita", "Anirban")
print(students[0])
print(students[2])
print(students[-1])
print(students[-2])
# Output:
# Tarun
# Pritam
# Anirban
# Ashmita
# Slicing
students = ("Tarun", "Alinda", "Pritam", "Ashmita", "Anirban", "Subhoraj")
print(students[1: 4])
# Output:
# ('Alinda', 'Pritam', 'Ashmita')
print(students[: 3])
# Output:
# ('Tarun', 'Alinda', 'Pritam')
print(students[3: ])
# Output:
# ('Ashmita', 'Anirban', 'Subhoraj')
print(students[:: 2])
# Output:
# ('Tarun', 'Pritam', 'Anirban')
print(students[:: -1])
# Output:
# ('Subhoraj', 'Anirban', 'Ashmita', 'Pritam', 'Alinda', 'Tarun')


# Tuple concatenation
a = ("Tarun", "Alinda")
b = ("Pritam", "Ashmita")
c = a + b
print(c)
# Output:
# ('Tarun', 'Alinda', 'Pritam', 'Ashmita')


# Tuple repetition
students = ("Tarun", "Alinda")
print(students * 3)
# Output:
# ('Tarun', 'Alinda', 'Tarun', 'Alinda', 'Tarun', 'Alinda')


# Single element tuple
student = ("Tarun", )
print(student)
# Output:
# ('Tarun', )



# Without comma it is not a tuple
student = ("Tarun")
print(type(student))
# Output:
# <class 'str'>
# With comma

student = ("Tarun", )
print(type(student))
# Output:
# <class 'tuple'>


# Empty tuple
students = ()
print(students)
# Output:
# ()
# type()
students = ("Tarun", "Alinda", "Pritam")
print(type(students))
# Output:
# <class 'tuple'>


# Tuple packing
students = "Tarun", "Alinda", "Pritam"
print(students)
# Output:
# ('Tarun', 'Alinda', 'Pritam')


# Tuple unpacking
students = ("Tarun", "Alinda", "Pritam")
a, b, c = students
print(a)
print(b)
print(c)
# Output:
# Tarun
# Alinda
# Pritam


# Extended unpacking
students = ("Tarun", "Alinda", "Pritam", "Ashmita", "Anirban")
a, *b, c = students
print(a)
print(b)
print(c)
# Output:
# Tarun
# ['Alinda', 'Pritam', 'Ashmita']
# Anirban


# Extended unpacking with first and last
students = ("Tarun", "Alinda", "Pritam", "Ashmita", "Anirban")
first, *middle, last = students
print(first)
print(middle)
print(last)
# Output:
# Tarun
# ['Alinda', 'Pritam', 'Ashmita']
# Anirban


# Converting list to tuple
students = ["Tarun", "Alinda", "Pritam"]
students = tuple(students)
print(students)
# Output:
# ('Tarun', 'Alinda', 'Pritam')


# Converting tuple to list
students = ("Tarun", "Alinda", "Pritam")
students = list(students)
print(students)
# Output:
# ['Tarun', 'Alinda', 'Pritam']


# Sorting tuple
marks = (78, 92, 65, 88, 70)
new_marks = sorted(marks)
print(new_marks)
# Output:
# [65, 70, 78, 88, 92]


# Sorting tuple in descending order
marks = (78, 92, 65, 88, 70)
new_marks = sorted(marks, reverse=True)
print(new_marks)
# Output:
# [92, 88, 78, 70, 65]


# reversed()
students = ("Tarun", "Alinda", "Pritam", "Ashmita")
new_students = tuple(reversed(students))
print(new_students)
# Output:
# ('Ashmita', 'Pritam', 'Alinda', 'Tarun')


# Nested tuple
students = (
("Tarun", 78),
("Alinda", 92),
("Pritam", 65),
("Ashmita", 88)
)
print(students)
# Output:
# (('Tarun', 78), ('Alinda', 92), ('Pritam', 65), ('Ashmita', 88))
# Accessing nested tuple
students = (
("Tarun", 78),
("Alinda", 92),
("Pritam", 65)
)
print(students[0])
print(students[0][0])
print(students[0][1])
# Output:
# ('Tarun', 78)
# Tarun
# 78



# Tuple containing different data types
student = ("Tarun", 22, 85.5, True)
print(student)
# Output:
# ('Tarun', 22, 85. 5, True)


# Tuple can contain a list
student = ("Tarun", 22, ["Python", "Java"])
print(student)
# Output:
# ('Tarun', 22, ['Python', 'Java'])


# Changing the list inside tuple
student = ("Tarun", 22, ["Python", "Java"])
student[2]. append("SQL")
print(student)
# Output:
# ('Tarun', 22, ['Python', 'Java', 'SQL'])


# Tuple itself cannot be changed
students = ("Tarun", "Alinda", "Pritam")
# students[0] = "Ashmita"
print(students)
# Output:
# ('Tarun', 'Alinda', 'Pritam')


# Finding length of nested tuple
students = (
("Tarun", 20),
("Alinda", 21),
("Pritam", 22)
)
print(len(students))
# Output:
# 3



# Tuple comparison
a = (10, 20, 30)
b = (10, 20, 30)
print(a == b)
# Output:
# True



# Tuple comparison
a = (10, 20, 30)
b = (10, 20, 40)
print(a == b)
# Output:
# False



# Tuple comparison follows order
a = ("Tarun", "Alinda")
b = ("Alinda", "Tarun")
print(a == b)
# Output:
# False



# Tuple as dictionary key
student = ("Tarun", 22)
data = {
student: "Python Student"
}
print(data)
# Output:
# {('Tarun', 22): 'Python Student'}


# Tuple as set element
students = {
("Tarun", 22),
("Alinda", 21),
("Pritam", 23)
}
print(students)
# Output:
# {('Tarun', 22), ('Alinda', 21), ('Pritam', 23)}


# for loop with tuple
students = ("Tarun", "Alinda", "Pritam", "Ashmita")
for student in students:
    print(student)
# Output:
# Tarun
# Alinda
# Pritam
# Ashmita


# enumerate() with tuple
students = ("Tarun", "Alinda", "Pritam", "Ashmita")
for index, student in enumerate(students):
    print(index, student)
# Output:
# 0 Tarun
# 1 Alinda
# 2 Pritam
# 3 Ashmita


# zip() with tuples
names = ("Tarun", "Alinda", "Pritam")
marks = (78, 92, 85)
students = tuple(zip(names, marks))
print(students)
# Output:
# (('Tarun', 78), ('Alinda', 92), ('Pritam', 85))
# Tuple unpacking with zip()
names = ("Tarun", "Alinda", "Pritam")
marks = (78, 92, 85)
for name, mark in zip(names, marks):
   print(name, mark)
# Output:
# Tarun 78
# Alinda 92
# Pritam 85
# any()
marks = (0, 0, 85, 0)
print(any(marks))
# Output:
# True


# all()
marks = (85, 78, 92, 88)
print(all(marks))
# Output:
# True


# all() with zero
marks = (85, 78, 0, 88)
print(all(marks))
# Output:
# False


# tuple() from string
name = "Tarun"
letters = tuple(name)
print(letters)
# Output:
# ('T', 'a', 'r', 'u', 'n')


# tuple() from range
numbers = tuple(range(1, 6))
print(numbers)
# Output:
# (1, 2, 3, 4, 5)

# Tuple with range
numbers = tuple(range(2, 11, 2))
print(numbers)
# Output:
# (2, 4, 6, 8, 10)
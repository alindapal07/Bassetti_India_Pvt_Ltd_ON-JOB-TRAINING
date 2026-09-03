# SET

# add() - adds one element
students = {"Tarun", "Alinda", "Pritam"}
students.add("Ashmita")
print(students)

# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita'}


# update() - adds multiple elements
students = {"Tarun", "Alinda"}
students.update(["Pritam", "Ashmita", "Anirban"])
print(students)

# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita', 'Anirban'}


# remove() - removes an element
students = {"Tarun", "Alinda", "Pritam"}
students.remove("Pritam")
print(students)

# Output:
# {'Tarun', 'Alinda'}


# discard() - removes an element if present
students = {"Tarun", "Alinda", "Pritam"}
students.discard("Pritam")
print(students)

# Output:
# {'Tarun', 'Alinda'}


# pop() - removes a random element
students = {"Tarun", "Alinda", "Pritam"}
student = students.pop()
print(student)
print(students)

# Output:
# Alinda
# {'Tarun', 'Pritam'}


# clear() - removes all elements
students = {"Tarun", "Alinda", "Pritam"}
students.clear()
print(students)

# Output:
# set()


# copy() - creates a copy
students = {"Tarun", "Alinda", "Pritam"}
new_students = students.copy()
print(new_students)

# Output:
# {'Tarun', 'Alinda', 'Pritam'}


# union() - combines two sets
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita", "Anirban"}
print(a.union(b))

# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita', 'Anirban'}


# intersection() - gives common elements
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita", "Tarun"}
print(a.intersection(b))

# Output:
# {'Tarun', 'Pritam'}


# difference() - gives elements only in first set
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a.difference(b))

# Output:
# {'Tarun', 'Alinda'}


# symmetric_difference() - gives elements not common
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a.symmetric_difference(b))

# Output:
# {'Tarun', 'Alinda', 'Ashmita'}


# intersection_update() - keeps only common elements
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
a.intersection_update(b)
print(a)

# Output:
# {'Pritam'}


# difference_update() - removes common elements
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
a.difference_update(b)
print(a)

# Output:
# {'Tarun', 'Alinda'}


# symmetric_difference_update() - keeps non-common elements
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
a.symmetric_difference_update(b)
print(a)

# Output:
# {'Tarun', 'Alinda', 'Ashmita'}


# issubset() - checks if set is inside another set
a = {"Tarun", "Alinda"}
b = {"Tarun", "Alinda", "Pritam"}
print(a.issubset(b))

# Output:
# True


# issuperset() - checks if set contains another set
a = {"Tarun", "Alinda", "Pritam"}
b = {"Tarun", "Alinda"}
print(a.issuperset(b))

# Output:
# True


# isdisjoint() - checks if sets have no common elements
a = {"Tarun", "Alinda"}
b = {"Pritam", "Ashmita"}
print(a.isdisjoint(b))

# Output:
# True


# in - checks if element exists
students = {"Tarun", "Alinda", "Pritam"}
print("Tarun" in students)

# Output:
# True


# not in - checks if element does not exist
students = {"Tarun", "Alinda", "Pritam"}
print("Ashmita" not in students)

# Output:
# True


# len() - returns number of elements
students = {"Tarun", "Alinda", "Pritam", "Ashmita"}
print(len(students))

# Output:
# 4


# max() - returns biggest value
marks = {78, 92, 65, 88, 70}
print(max(marks))

# Output:
# 92


# min() - returns smallest value
marks = {78, 92, 65, 88, 70}
print(min(marks))

# Output:
# 65


# sum() - returns total value
marks = {78, 92, 65, 88, 70}
print(sum(marks))

# Output:
# 393


# sorted() - returns sorted list
marks = {78, 92, 65, 88, 70}
print(sorted(marks))

# Output:
# [65, 70, 78, 88, 92]


# | - performs union
a = {"Tarun", "Alinda"}
b = {"Pritam", "Ashmita"}
print(a | b)

# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita'}


# & - performs intersection
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a & b)

# Output:
# {'Pritam'}


# - - performs difference
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a - b)

# Output:
# {'Tarun', 'Alinda'}


# ^ - performs symmetric difference
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a ^ b)

# Output:
# {'Tarun', 'Alinda', 'Ashmita'}


# FROZENSET

# frozenset() - creates an immutable set
students = frozenset(["Tarun", "Alinda", "Pritam"])
print(students)

# Output:
# frozenset({'Tarun', 'Alinda', 'Pritam'})


# union() - combines two frozensets
a = frozenset(["Tarun", "Alinda"])
b = frozenset(["Pritam", "Ashmita"])
print(a.union(b))

# Output:
# frozenset({'Tarun', 'Alinda', 'Pritam', 'Ashmita'})


# intersection() - gives common elements
a = frozenset(["Tarun", "Alinda", "Pritam"])
b = frozenset(["Pritam", "Ashmita"])
print(a.intersection(b))

# Output:
# frozenset({'Pritam'})


# difference() - gives elements only in first set
a = frozenset(["Tarun", "Alinda", "Pritam"])
b = frozenset(["Pritam", "Ashmita"])
print(a.difference(b))

# Output:
# frozenset({'Tarun', 'Alinda'})


# symmetric_difference() - gives non-common elements
a = frozenset(["Tarun", "Alinda", "Pritam"])
b = frozenset(["Pritam", "Ashmita"])
print(a.symmetric_difference(b))

# Output:
# frozenset({'Tarun', 'Alinda', 'Ashmita'})


# issubset() - checks if set is inside another set
a = frozenset(["Tarun", "Alinda"])
b = frozenset(["Tarun", "Alinda", "Pritam"])
print(a.issubset(b))

# Output:
# True


# issuperset() - checks if set contains another set
a = frozenset(["Tarun", "Alinda", "Pritam"])
b = frozenset(["Tarun", "Alinda"])
print(a.issuperset(b))

# Output:
# True


# isdisjoint() - checks if sets have no common elements
a = frozenset(["Tarun", "Alinda"])
b = frozenset(["Pritam", "Ashmita"])
print(a.isdisjoint(b))

# Output:
# True


# in - checks if element exists
students = frozenset(["Tarun", "Alinda", "Pritam"])
print("Tarun" in students)

# Output:
# True


# len() - returns number of elements
students = frozenset(["Tarun", "Alinda", "Pritam"])
print(len(students))

# Output:
# 3


# max() - returns biggest value
marks = frozenset([78, 92, 65, 88, 70])
print(max(marks))

# Output:
# 92


# min() - returns smallest value
marks = frozenset([78, 92, 65, 88, 70])
print(min(marks))

# Output:
# 65


# sum() - returns total value
marks = frozenset([78, 92, 65, 88, 70])
print(sum(marks))

# Output:
# 393


# sorted() - returns sorted list
marks = frozenset([78, 92, 65, 88, 70])
print(sorted(marks))

# Output:
# [65, 70, 78, 88, 92]


# | - performs union
a = frozenset(["Tarun", "Alinda"])
b = frozenset(["Pritam", "Ashmita"])
print(a | b)

# Output:
# frozenset({'Tarun', 'Alinda', 'Pritam', 'Ashmita'})


# & - performs intersection
a = frozenset(["Tarun", "Alinda", "Pritam"])
b = frozenset(["Pritam", "Ashmita"])
print(a & b)

# Output:
# frozenset({'Pritam'})


# - - performs difference
a = frozenset(["Tarun", "Alinda", "Pritam"])
b = frozenset(["Pritam", "Ashmita"])
print(a - b)

# Output:
# frozenset({'Tarun', 'Alinda'})


# ^ - performs symmetric difference
a = frozenset(["Tarun", "Alinda", "Pritam"])
b = frozenset(["Pritam", "Ashmita"])
print(a ^ b)

# Output:
# frozenset({'Tarun', 'Alinda', 'Ashmita'})
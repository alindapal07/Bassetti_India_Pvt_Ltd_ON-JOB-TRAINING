# SET OPERATIONS

# union() - combines elements of both sets
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita", "Anirban"}
print(a.union(b))
# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita', 'Anirban'}

# | - combines elements of both sets
a = {"Tarun", "Alinda"}
b = {"Pritam", "Ashmita"}
print(a | b)
# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita'}

# intersection() - gives common elements
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita", "Tarun"}
print(a.intersection(b))
# Output:
# {'Tarun', 'Pritam'}

# & - gives common elements
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a & b)
# Output:
# {'Pritam'}

# difference() - gives elements only from first set
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a.difference(b))
# Output:
# {'Tarun', 'Alinda'}

# - - gives elements only from first set
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a - b)
# Output:
# {'Tarun', 'Alinda'}

# symmetric_difference() - gives elements that are not common
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a.symmetric_difference(b))
# Output:
# {'Tarun', 'Alinda', 'Ashmita'}

# ^ - gives elements that are not common
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
print(a ^ b)
# Output:
# {'Tarun', 'Alinda', 'Ashmita'}

# intersection_update() - keeps only common elements in first set
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
a.intersection_update(b)
print(a)
# Output:
# {'Pritam'}

# difference_update() - removes common elements from first set
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
a.difference_update(b)
print(a)
# Output:
# {'Tarun', 'Alinda'}

# symmetric_difference_update() - updates first set with non-common elements
a = {"Tarun", "Alinda", "Pritam"}
b = {"Pritam", "Ashmita"}
a.symmetric_difference_update(b)
print(a)
# Output:
# {'Tarun', 'Alinda', 'Ashmita'}

# issubset() - checks if all elements are present in another set
a = {"Tarun", "Alinda"}
b = {"Tarun", "Alinda", "Pritam"}
print(a.issubset(b))
# Output:
# True

# issuperset() - checks if a set contains all elements of another set
a = {"Tarun", "Alinda", "Pritam"}
b = {"Tarun", "Alinda"}
print(a.issuperset(b))
# Output:
# True

# isdisjoint() - checks if two sets have no common elements
a = {"Tarun", "Alinda"}
b = {"Pritam", "Ashmita"}
print(a.isdisjoint(b))
# Output:
# True

# in - checks if an element is present
students = {"Tarun", "Alinda", "Pritam"}
print("Tarun" in students)
# Output:
# True

# not in - checks if an element is not present
students = {"Tarun", "Alinda", "Pritam"}
print("Ashmita" not in students)
# Output:
# True

# add() - adds one element
students = {"Tarun", "Alinda", "Pritam"}
students.add("Ashmita")
print(students)
# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita'}

# update() - adds multiple elements
students = {"Tarun", "Alinda"}
students.update(["Pritam", "Ashmita"])
print(students)
# Output:
# {'Tarun', 'Alinda', 'Pritam', 'Ashmita'}

# remove() - removes an element
students = {"Tarun", "Alinda", "Pritam"}
students.remove("Pritam")
print(students)
# Output:
# {'Tarun', 'Alinda'}

# discard() - removes an element if it exists
students = {"Tarun", "Alinda", "Pritam"}
students.discard("Pritam")
print(students)
# Output:
# {'Tarun', 'Alinda'}
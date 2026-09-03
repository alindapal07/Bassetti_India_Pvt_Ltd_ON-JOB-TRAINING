# DICTIONARY

# get() - gets value using key
student = {"name": "Tarun", "age": 22, "course": "Python"}
print(student.get("name"))
# Output:
# Tarun

# get() - returns default value if key is missing
student = {"name": "Tarun", "age": 22}
print(student.get("marks", 0))
# Output:
# 0

# keys() - returns all keys
student = {"name": "Tarun", "age": 22, "course": "Python"}
print(student.keys())
# Output:
# dict_keys(['name', 'age', 'course'])

# values() - returns all values
student = {"name": "Tarun", "age": 22, "course": "Python"}
print(student.values())
# Output:
# dict_values(['Tarun', 22, 'Python'])

# items() - returns key-value pairs
student = {"name": "Tarun", "age": 22, "course": "Python"}
print(student.items())
# Output:
# dict_items([('name', 'Tarun'), ('age', 22), ('course', 'Python')])

# pop() - removes a key and returns its value
student = {"name": "Tarun", "age": 22, "course": "Python"}
value = student.pop("age")
print(value)
print(student)
# Output:
# 22
# {'name': 'Tarun', 'course': 'Python'}

# pop() - returns default value if key is missing
student = {"name": "Tarun", "age": 22}
value = student.pop("marks", 0)
print(value)
print(student)
# Output:
# 0
# {'name': 'Tarun', 'age': 22}

# popitem() - removes the last key-value pair
student = {"name": "Tarun", "age": 22, "course": "Python"}
value = student.popitem()
print(value)
print(student)
# Output:
# ('course', 'Python')
# {'name': 'Tarun', 'age': 22}

# update() - adds or changes key-value pairs
student = {"name": "Tarun", "age": 22}
student.update({"course": "Python"})
print(student)
# Output:
# {'name': 'Tarun', 'age': 22, 'course': 'Python'}

# update() - changes an existing value
student = {"name": "Tarun", "age": 22}
student.update({"age": 23})
print(student)
# Output:
# {'name': 'Tarun', 'age': 23}

# setdefault() - gets value or adds a new key
student = {"name": "Tarun", "age": 22}
value = student.setdefault("course", "Python")
print(value)
print(student)
# Output:
# Python
# {'name': 'Tarun', 'age': 22, 'course': 'Python'}

# setdefault() - keeps existing value
student = {"name": "Tarun", "age": 22}
value = student.setdefault("name", "Alinda")
print(value)
print(student)
# Output:
# Tarun
# {'name': 'Tarun', 'age': 22}

# clear() - removes all key-value pairs
student = {"name": "Tarun", "age": 22, "course": "Python"}
student.clear()
print(student)
# Output:
# {}

# copy() - creates a copy of dictionary
student = {"name": "Tarun", "age": 22}
new_student = student.copy()
print(new_student)
# Output:
# {'name': 'Tarun', 'age': 22}

# fromkeys() - creates dictionary from keys
keys = ["name", "age", "course"]
student = dict.fromkeys(keys)
print(student)
# Output:
# {'name': None, 'age': None, 'course': None}

# fromkeys() - gives same value to all keys
keys = ["name", "age", "course"]
student = dict.fromkeys(keys, "Not Available")
print(student)
# Output:
# {'name': 'Not Available', 'age': 'Not Available', 'course': 'Not Available'}

# [] - gets value using key
student = {"name": "Tarun", "age": 22}
print(student["name"])
# Output:
# Tarun

# [] - adds a new key-value pair
student = {"name": "Tarun", "age": 22}
student["course"] = "Python"
print(student)
# Output:
# {'name': 'Tarun', 'age': 22, 'course': 'Python'}

# [] - changes value of a key
student = {"name": "Tarun", "age": 22}
student["age"] = 23
print(student)
# Output:
# {'name': 'Tarun', 'age': 23}

# del - removes a key-value pair
student = {"name": "Tarun", "age": 22, "course": "Python"}
del student["age"]
print(student)
# Output:
# {'name': 'Tarun', 'course': 'Python'}

# in - checks if key exists
student = {"name": "Tarun", "age": 22}
print("name" in student)
# Output:
# True

# not in - checks if key does not exist
student = {"name": "Tarun", "age": 22}
print("marks" not in student)
# Output:
# True

# len() - returns number of key-value pairs
student = {"name": "Tarun", "age": 22, "course": "Python"}
print(len(student))
# Output:
# 3

# max() - returns biggest key
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(max(marks))
# Output:
# Tarun

# min() - returns smallest key
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(min(marks))
# Output:
# Alinda

# max() - returns key with highest value
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(max(marks, key=marks.get))
# Output:
# Alinda

# min() - returns key with lowest value
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(min(marks, key=marks.get))
# Output:
# Tarun

# sorted() - returns sorted keys
marks = {"Pritam": 85, "Tarun": 78, "Alinda": 92}
print(sorted(marks))
# Output:
# ['Alinda', 'Pritam', 'Tarun']

# sorted() - sorts keys using values
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(sorted(marks, key=marks.get))
# Output:
# ['Tarun', 'Pritam', 'Alinda']

# sorted() - sorts values from high to low
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(sorted(marks, key=marks.get, reverse=True))
# Output:
# ['Alinda', 'Pritam', 'Tarun']

# sum() - adds all dictionary values
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(sum(marks.values()))
# Output:
# 255

# any() - checks if any value is true
marks = {"Tarun": 0, "Alinda": 0, "Pritam": 85}
print(any(marks.values()))
# Output:
# True

# all() - checks if all values are true
marks = {"Tarun": 78, "Alinda": 92, "Pritam": 85}
print(all(marks.values()))
# Output:
# True

# zip() - combines two lists into dictionary
names = ["Tarun", "Alinda", "Pritam"]
marks = [78, 92, 85]
students = dict(zip(names, marks))
print(students)
# Output:
# {'Tarun': 78, 'Alinda': 92, 'Pritam': 85}

# dictionary comprehension - creates dictionary using expression
numbers = [1, 2, 3, 4, 5]
squares = {x: x * x for x in numbers}
print(squares)
# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# dictionary comprehension - creates dictionary with condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = {x: x * x for x in numbers if x % 2 == 0}
print(even_numbers)
# Output:
# {2: 4, 4: 16, 6: 36}

# nested dictionary - stores dictionary inside dictionary
students = {"student1": {"name": "Tarun", "age": 22}}
print(students["student1"]["name"])
# Output:
# Tarun

# nested dictionary - changes inner value
students = {"student1": {"name": "Tarun", "age": 22}}
students["student1"]["age"] = 23
print(students)
# Output:
# {'student1': {'name': 'Tarun', 'age': 23}}

# items() with loop - gets key and value together
student = {"name": "Tarun", "age": 22, "course": "Python"}
for key, value in student.items():
    print(key, value)
# Output:
# name Tarun
# age 22
# course Python

# values() with loop - gets each value
student = {"name": "Tarun", "age": 22, "course": "Python"}
for value in student.values():
    print(value)
# Output:
# Tarun
# 22
# Python

# keys() with loop - gets each key
student = {"name": "Tarun", "age": 22, "course": "Python"}
for key in student.keys():
    print(key)
# Output:
# name
# age
# course
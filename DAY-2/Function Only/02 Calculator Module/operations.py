# Calculator Operations Module


# Addition using *args
def add(*args):
    return sum(args)


# Subtraction using *args
def subtract(*args):
    result = args[0]

    for num in args[1:]:
        result = result - num

    return result


# Multiplication using *args
def multiply(*args):
    result = 1

    for num in args:
        result = result * num

    return result


# Division using *args
def divide(*args):
    result = args[0]

    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        result = result / num

    return result
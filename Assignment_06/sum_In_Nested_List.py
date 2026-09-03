def total(data):
    sum = 0

    for item in data:
        if type(item) in (int, float):
            sum += item
        elif type(item) == list:
            sum += total(item)

    return sum


nums = eval(input("Enter list: "))

print(total(nums))

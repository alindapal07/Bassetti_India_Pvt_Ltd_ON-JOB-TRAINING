def flat_dict(data, sep):
    result = {}

    def flat(d, name=""):
        for key, value in d.items():
            new_name = name + sep + key if name else key

            if type(value) == dict:
                flat(value, new_name)
            else:
                result[new_name] = value

    flat(data)
    return result


data = eval(input("Enter dictionary: "))
sep = input("Enter separator: ")

print(flat_dict(data, sep))


def validate_id(value):
    if not value.isdigit():
        raise ValueError("ID must be a number")

    value = int(value)

    if value <= 0:
        raise ValueError("ID must be positive")

    return value

def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")

    return name.strip()

def validate_text(value, field):
    if not value.strip():
        raise ValueError(field + " cannot be empty")

    return value.strip()
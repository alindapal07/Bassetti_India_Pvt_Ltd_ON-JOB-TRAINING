def validate_pin(pin):
    if len(pin) != 4:
        raise ValueError("PIN must contain exactly 4 digits")

    if not pin.isdigit():
        raise ValueError("PIN must contain only digits")

    return True
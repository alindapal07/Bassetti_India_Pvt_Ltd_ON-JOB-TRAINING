balance = 5000
pin = "1234"

def check_balance():
    return balance

def withdraw(amount):
    global balance

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    if amount % 100 != 0:
        raise ValueError("Withdrawal amount must be a multiple of 100")

    balance -= amount
    return balance

def deposit(amount):
    global balance

    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    balance += amount
    return balance

def change_pin(old_pin, new_pin):
    global pin

    if old_pin != pin:
        raise ValueError("Incorrect current PIN")

    if len(new_pin) != 4 or not new_pin.isdigit():
        raise ValueError("PIN must contain exactly 4 digits")

    if new_pin == pin:
        raise ValueError("New PIN cannot be same as old PIN")

    pin = new_pin
    return "PIN changed successfully"
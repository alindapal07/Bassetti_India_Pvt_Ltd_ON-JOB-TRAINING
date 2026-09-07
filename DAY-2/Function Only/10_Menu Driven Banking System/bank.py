accounts = {
    "ACC1001": {
        "account_number": "ACC1001",
        "name": "Poku",
        "balance": 5000
    }
}

class InvalidAccountError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class DuplicateAccountError(Exception):
    pass

def create_account(account_number, name, balance):
    if account_number in accounts:
        raise DuplicateAccountError("Account number already exists")

    if balance < 0:
        raise NegativeAmountError("Initial balance cannot be negative")

    accounts[account_number] = {
        "account_number": account_number,
        "name": name,
        "balance": balance
    }

    return "Account created successfully"

def deposit(account_number, amount):
    if account_number not in accounts:
        raise InvalidAccountError("Invalid account number")

    if amount <= 0:
        raise NegativeAmountError("Amount must be positive")

    accounts[account_number]["balance"] += amount
    return "Amount deposited successfully"

def withdraw(account_number, amount):
    if account_number not in accounts:
        raise InvalidAccountError("Invalid account number")

    if amount <= 0:
        raise NegativeAmountError("Amount must be positive")

    if amount > accounts[account_number]["balance"]:
        raise InsufficientBalanceError("Insufficient balance")

    accounts[account_number]["balance"] -= amount
    return "Amount withdrawn successfully"

def transfer(from_account, to_account, amount):
    if from_account not in accounts:
        raise InvalidAccountError("Sender account does not exist")

    if to_account not in accounts:
        raise InvalidAccountError("Receiver account does not exist")

    if amount <= 0:
        raise NegativeAmountError("Amount must be positive")

    if amount > accounts[from_account]["balance"]:
        raise InsufficientBalanceError("Insufficient balance")

    accounts[from_account]["balance"] -= amount
    accounts[to_account]["balance"] += amount

    return "Amount transferred successfully"

def get_balance(account_number):
    if account_number not in accounts:
        raise InvalidAccountError("Invalid account number")

    return accounts[account_number]["balance"]
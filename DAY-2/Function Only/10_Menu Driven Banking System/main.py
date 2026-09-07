# Menu-Driven Banking System
#
# Use dictionaries and functions.
#
# Support:
# 1. Create account
# 2. Deposit
# 3. Withdraw
# 4. Check balance
# 5. Transfer
# 6. Exit
#
# Example account:
# {
#     "account_number": "ACC1001",
#     "name": "Poku",
#     "balance": 5000
# }
#
# Create functions:
# create_account()
# deposit()
# withdraw()
# transfer()
# get_balance()
#
# Handle:
# - Invalid account
# - Negative amount
# - Insufficient balance
# - Duplicate account number
#



from bank import (
    create_account,
    deposit,
    withdraw,
    transfer,
    get_balance,
    InvalidAccountError,
    NegativeAmountError,
    InsufficientBalanceError,
    DuplicateAccountError
)

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Transfer")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            account_number = input("Enter account number: ")
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))

            print(create_account(account_number, name, balance))

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount: "))

            print(deposit(account_number, amount))

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount: "))

            print(withdraw(account_number, amount))

        elif choice == "4":
            account_number = input("Enter account number: ")

            balance = get_balance(account_number)
            print("Current balance:", balance)

        elif choice == "5":
            from_account = input("Enter sender account: ")
            to_account = input("Enter receiver account: ")
            amount = float(input("Enter amount: "))

            print(transfer(from_account, to_account, amount))

        elif choice == "6":
            print("Thank you for using the banking system!")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid amount. Please enter a number.")

    except InvalidAccountError as e:
        print("Account Error:", e)

    except NegativeAmountError as e:
        print("Amount Error:", e)

    except InsufficientBalanceError as e:
        print("Transaction Error:", e)

    except DuplicateAccountError as e:
        print("Account Error:", e)
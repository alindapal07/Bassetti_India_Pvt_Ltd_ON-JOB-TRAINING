from operations import (
    pin,
    check_balance,
    withdraw,
    deposit,
    change_pin
)
from validators import validate_pin

def login():
    attempts = 0

    while attempts < 3:
        entered_pin = input("Enter PIN: ")

        try:
            validate_pin(entered_pin)

            if entered_pin == pin:
                print("Login successful")
                return True

            attempts += 1
            print("Incorrect PIN")
            print("Attempts remaining:", 3 - attempts)

        except ValueError as e:
            attempts += 1
            print("Invalid PIN:", e)
            print("Attempts remaining:", 3 - attempts)

    print("Maximum attempts exceeded. Account blocked.")
    return False

if login():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                print("Current balance:", check_balance())

            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                print("Remaining balance:", withdraw(amount))

            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                print("Current balance:", deposit(amount))

            elif choice == "4":
                old_pin = input("Enter current PIN: ")
                new_pin = input("Enter new PIN: ")
                validate_pin(new_pin)
                print(change_pin(old_pin, new_pin))

            elif choice == "5":
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid choice")

        except ValueError as e:
            print("Error:", e)
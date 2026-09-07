# Calculator Main Program

# Calculator Module
#
# Create:
#
# calculator/
# ├── main.py
# └── operations.py
#
# operations.py should contain:
#
# 1. add()
# 2. subtract()
# 3. multiply()
# 4. divide()
#
# main.py should:
#
# 1. Take user input
# 2. Perform the selected operation
# 3. Handle invalid numbers
# 4. Handle invalid operations
# 5. Handle division by zero









from operations import add, subtract, multiply, divide


print("----- CALCULATOR -----")

try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = add(num1, num2)

    elif choice == "2":
        result = subtract(num1, num2)

    elif choice == "3":
        result = multiply(num1, num2)

    elif choice == "4":
        result = divide(num1, num2)

    else:
        raise ValueError("Invalid operation")

    print("Result:", result)


except ValueError as e:
    print("Error:", e)

except ZeroDivisionError as e:
    print("Error:", e)
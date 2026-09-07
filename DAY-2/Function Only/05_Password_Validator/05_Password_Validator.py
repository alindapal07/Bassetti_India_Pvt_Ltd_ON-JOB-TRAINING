# Password Validator
#
# Create:
#
# validate_password(password)
#
# Password requirements:
#
# - Minimum 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one number
# - At least one special character
#
# Example:
#
# Password: Hello123
#
# Output:
#
# Invalid password:
# - Missing special character


def validate_password(password) -> str:
    if len(password) < 8:
        raise ValueError("Password should have length of at least 8 characters")
    uppercase = lowercase = number = specialChar = 0
    for ch in password:
        if ch.isalpha():
            if ch.isupper():
                uppercase += 1
            else:
                lowercase += 1
        elif ch.isdigit():
            number += 1
        else:
            specialChar += 1
    if uppercase < 1:
        raise ValueError("Missing uppercase character")
    if lowercase < 1:
        raise ValueError("Missing lowercase character")
    if number < 1:
        raise ValueError("Missing number")
    if specialChar < 1:
        raise ValueError("Missing special character")
    return "Valid password"


# Main program
try:
    password = input("Enter password: ")
    if isinstance(password, str):
        result = validate_password(password)
        print(result)
    else:
        raise ValueError("Password must be a string")
except ValueError as e:
    print("Invalid password:", e)
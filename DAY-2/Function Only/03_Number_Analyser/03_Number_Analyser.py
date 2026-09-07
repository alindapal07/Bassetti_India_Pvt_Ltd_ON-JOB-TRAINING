# Number Analyzer
#
# Create the following functions:
#
# 1. is_prime()
# 2. is_even()
# 3. is_odd()
# 4. get_factors()
# 5. get_prime_factors()
#
# Given a number:
#
# Enter number: 84
#
# Output:
#
# Even: Yes
# Prime: No
# Factors: [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84]
# Prime Factors: [2, 3, 7]
#
# Handle:
#
# - Negative numbers
# - Zero
# - One
# - Invalid input


# Number Analyzer


# Check whether number is even
def is_even(num):
    return num % 2 == 0


# Check whether number is odd
def is_odd(num):
    return num % 2 != 0

# Check whether number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Get all factors of a number
def get_factors(num):
    factors = []
    num = abs(num)
    if num == 0:
        return factors
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors


# Get prime factors
def get_prime_factors(num):
    prime_factors = []
    num = abs(num)
    if num <= 1:
        return prime_factors
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors.append(i)
    return prime_factors


# Main program

try:

    num = int(input("Enter number: "))

    # Handle zero
    if num == 0:
        print("Zero: Yes")
        print("Even: Yes")
        print("Odd: No")
        print("Prime: No")
        print("Factors: []")
        print("Prime Factors: []")

    else:

        # Convert negative number to positive
        number = abs(num)
        print("Even:", "Yes" if is_even(number) else "No")
        print("Odd:", "Yes" if is_odd(number) else "No")
        print("Prime:", "Yes" if is_prime(number) else "No")
        print("Factors:", get_factors(number))
        print("Prime Factors:", get_prime_factors(number))

except ValueError:
    print("Invalid input! Please enter a valid integer.")
# Assignment 18: Expense Report Generator
#
# Given:
# expenses = [
#     {"category": "Food", "amount": 500},
#     {"category": "Travel", "amount": 1000},
#     {"category": "Food", "amount": 300},
#     {"category": "Shopping", "amount": 2000}
# ]
#
# Generate:
# Total Expense: ₹3800
# Food: ₹800
# Travel: ₹1000
# Shopping: ₹2000
# Highest Category: Shopping
#
# Functions should include:
# - calculate_total()
# - group_by_category()
# - get_highest_category()
# - generate_report()
#
# Handle:
# - Empty expenses
# - Invalid amounts




expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1000},
    {"category": "Food", "amount": 300},
    {"category": "Shopping", "amount": 2000}
]

def calculate_total(expenses):
    if not expenses:
        return 0

    total = 0

    for expense in expenses:
        amount = expense["amount"]

        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount < 0:
            raise ValueError("Invalid expense amount")

        total += amount

    return total

def group_by_category(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount < 0:
            raise ValueError("Invalid expense amount")

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories

def get_highest_category(categories):
    if not categories:
        return None

    return max(categories, key=categories.get)

def generate_report(expenses):
    if not expenses:
        print("No expenses available")
        return

    total = calculate_total(expenses)
    categories = group_by_category(expenses)
    highest = get_highest_category(categories)

    print("Total Expense: ₹", total)

    for category, amount in categories.items():
        print(category + ": ₹", amount)

    print("Highest Category:", highest)

try:
    generate_report(expenses)
except ValueError as e:
    print("Error:", e)
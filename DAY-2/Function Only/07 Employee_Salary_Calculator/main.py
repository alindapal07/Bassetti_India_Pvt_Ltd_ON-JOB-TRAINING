# Employee Salary Calculator
#
# Input:
#
# employee = {
#     "name": "Ashmita",
#     "basic_salary": 100000,
#     "experience": 1
# }
#
# Calculate:
#
# 1. Basic Salary
# 2. HRA
# 3. DA
# 4. Bonus
# 5. Tax
# 6. Net Salary
#
# Create separate functions for each calculation.
#
# Structure:
#
# salary/
# ├── main.py
# ├── calculations.py
# └── validators.py



# Employee Salary Calculator

from calculations import (
    calculate_basic_salary,
    calculate_hra,
    calculate_da,
    calculate_bonus,
    calculate_gross_salary,
    calculate_tax,
    calculate_net_salary
)
from validators import (
    validate_salary,
    validate_experience
)

employee = {
    "name": "Ashmita",
    "basic_salary": 100000,
    "experience": 1
}

try:

    # Get employee details
    name = employee["name"]
    basic_salary = employee["basic_salary"]
    experience = employee["experience"]

    # Validate inputs
    validate_salary(basic_salary)
    validate_experience(experience)

    # Calculate salary components
    basic = calculate_basic_salary(basic_salary)
    hra = calculate_hra(basic)
    da = calculate_da(basic)
    bonus = calculate_bonus(basic, experience)
    gross_salary = calculate_gross_salary(
        basic,
        hra,
        da,
        bonus
    )
    tax = calculate_tax(gross_salary)
    net_salary = calculate_net_salary(
        gross_salary,
        tax
    )

    # Display salary details

    print("\n===== EMPLOYEE SALARY =====")

    print("Employee Name :", name)
    print("Experience    :", experience, "year(s)")

    print("Basic Salary  :", basic)
    print("HRA           :", hra)
    print("DA            :", da)
    print("Bonus         :", bonus)
    print("Gross Salary  :", gross_salary)
    print("Tax           :", tax)
    print("Net Salary    :", net_salary)

except (ValueError, TypeError) as e:

    print("Error:", e)
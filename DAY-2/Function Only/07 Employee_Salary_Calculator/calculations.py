# Salary Calculations

# Calculate Basic Salary
def calculate_basic_salary(basic_salary):
    return basic_salary
# Calculate HRA
def calculate_hra(basic_salary):
    return basic_salary * 0.20

# Calculate DA
def calculate_da(basic_salary):
    return basic_salary * 0.10
# Calculate Bonus
def calculate_bonus(basic_salary, experience):
    return basic_salary * 0.05 * experience

# Calculate Gross Salary
def calculate_gross_salary(basic_salary, hra, da, bonus):
    return basic_salary + hra + da + bonus

# Calculate Tax
def calculate_tax(gross_salary):
    return gross_salary * 0.10

# Calculate Net Salary
def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax
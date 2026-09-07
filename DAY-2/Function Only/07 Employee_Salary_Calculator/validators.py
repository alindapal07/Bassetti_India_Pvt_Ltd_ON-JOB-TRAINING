# Input Validators


def validate_salary(salary):
    if not isinstance(salary, (int, float)):
        raise TypeError("Salary must be a number")
    if salary <= 0:
        raise ValueError("Salary must be greater than 0")

def validate_experience(experience):
    if not isinstance(experience, (int, float)):
        raise TypeError("Experience must be a number")
    if experience < 0:
        raise ValueError("Experience cannot be negative")
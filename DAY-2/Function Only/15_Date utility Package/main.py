from utils import calculate_age, days_between_dates, is_leap_year, get_day_of_week, convert_to_date

try:
    dob_input = input("Enter DOB (YYYY-MM-DD): ")
    dob = convert_to_date(dob_input)

    print("Age:", calculate_age(dob))
    print("Day:", get_day_of_week(dob))
    print("Leap Year:", is_leap_year(dob.year))

    date1_input = input("Enter first date (YYYY-MM-DD): ")
    date2_input = input("Enter second date (YYYY-MM-DD): ")

    date1 = convert_to_date(date1_input)
    date2 = convert_to_date(date2_input)

    print("Days between dates:", days_between_dates(date1, date2))

except ValueError:
    print("Invalid date! Please use YYYY-MM-DD format.")
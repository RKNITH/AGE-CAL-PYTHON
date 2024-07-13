import time
from calendar import isleap as check_leap_year

def is_leap(year):
    return check_leap_year(year)

def days_in_month(month, leap):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap else 28

# Input date of birth
year = int(input("Please enter your year of birth (e.g., 2000): "))
month = int(input("Please enter your month of birth (e.g., 02): "))
day = int(input("Please enter your day of birth (e.g., 05): "))

current_time = time.localtime(time.time())

# Calculate age in years, months, and days
years = current_time.tm_year - year
months = current_time.tm_mon - month
days = current_time.tm_mday - day

# Adjust months and days if they are negative
if days < 0:
    months -= 1
    days += days_in_month(current_time.tm_mon - 1 if current_time.tm_mon > 1 else 12, is_leap(current_time.tm_year))
if months < 0:
    years -= 1
    months += 12

# Display the exact age
print(f"\n\tYour exact age is {years} years, {months} months, and {days} days.")

from datetime import datetime
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def calculate_progress(date_str):
    date = datetime.strptime(date_str, "%B %d, %Y %H:%M")
    days_in_month = [31, 29 if is_leap_year(date.year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_elapsed = sum(days_in_month[:date.month - 1]) + date.day - 1
    minutes_elapsed = days_elapsed * 1440 + date.hour * 60 + date.minute
    total_minutes = sum(days_in_month) * 1440

    return (minutes_elapsed / total_minutes) * 100

date_input = input()
print(f"{calculate_progress(date_input)}")

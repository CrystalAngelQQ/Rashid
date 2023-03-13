# # Python date
import datetime


# 1. Write a Python program to subtract five days from current date.
def subtract_five_days():
    today = datetime.datetime.today()
    five_days = datetime.timedelta(days=5)
    return today - five_days


print(f"Five days ago: {subtract_five_days()}")


# 2. Write a Python program to print yesterday, today, tomorrow.
def yesterday_today_tomorrow():
    today = datetime.datetime.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day
    tomorrow = today + one_day
    print(f"Yesterday: {yesterday}\nToday: {today}\nTomorrow: {tomorrow}")


yesterday_today_tomorrow()


# 3. Write a Python program to drop microseconds from datetime.
def drop_microseconds(date):
    date_without_microsecond = date.replace(microsecond=0)
    return date_without_microsecond


today_with_microseconds = datetime.datetime.today()
print(f"Date with microseconds: {today_with_microseconds}")
print(f"Date without microseconds: {drop_microseconds(today_with_microseconds)}")


# 4. Write a Python program to calculate two date difference in seconds.
def diff_in_seconds(date1, date2):
    date_diff = date1 - date2
    return date_diff.total_seconds()


print(
    f"Difference between 'after 10 days' and 'today', in seconds: {diff_in_seconds(today_with_microseconds + datetime.timedelta(days=10), today_with_microseconds)}"
)

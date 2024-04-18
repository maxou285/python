counts = 0
first_day_next_month = 1
# 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"

for year in range(1900, 2001):
    for month in range(1, 13):
        if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month = 29
        elif month == 2:
            days_in_month = 28
        elif month in [4, 6, 9, 11]:
            days_in_month = 30
        else:
            days_in_month = 31

        push = days_in_month % 7 + first_day_next_month
        first_day_next_month = push if push <= 6 else (push - 7)
        if year != 1900 and first_day_next_month == 6:
            counts += 1
if first_day_next_month == 6:
    counts -= 1
print(counts)

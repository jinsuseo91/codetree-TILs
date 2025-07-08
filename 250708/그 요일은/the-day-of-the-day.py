m1, d1, m2, d2 = map(int, input().split())
A = input().strip()

days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def date_diff(m1, d1, m2, d2):
    days = 0
    for m in range(m1, m2):
        days += days_in_month[m]
    days += d2 - d1
    return days

diff = date_diff(m1, d1, m2, d2)
count = 0
for i in range(diff + 1):
    if weekdays[i % 7] == A:
        count += 1

print(count)
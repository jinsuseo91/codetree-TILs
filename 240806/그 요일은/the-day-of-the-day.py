m1, d1, m2, d2 = map(int, input().split())
day = input()
days = 0
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(m1, m2):
    if i in [1, 3, 5, 7, 8, 10, 12] :
        days +=31
    elif i == 2 :
        days += 29
    else :
        days += 30

days = days + d2 - d1 + 1

n = 0
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

if day in day_list:
    n = day_list.index(day)

ans = (days - n) // 7 + 1
print(ans)
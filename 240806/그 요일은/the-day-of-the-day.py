m1, d1, m2, d2 = map(int, input().split())
day = input()
days = 0
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for i in range(m1, m2):
    days += num_of_days[i]
days = days + d2 - d1 + 1

n = day_list.index(day)

start_day_offset = (n + d1 - 1) % 7

total_day_occurrences = (days - (7 - start_day_offset) + 6) // 7 

# 결과 출력
print(total_day_occurrences)
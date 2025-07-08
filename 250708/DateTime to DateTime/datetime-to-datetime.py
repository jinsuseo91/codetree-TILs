a, b, c = map(int, input().split())

start_day = 11
start_hour = 11
start_minute = 11

start_total = start_day * 24 * 60 + start_hour * 60 + start_minute

target_total = a * 24 * 60 + b * 60 + c

diff = target_total - start_total

if diff < 0:
    print(-1)
else:
    print(diff)
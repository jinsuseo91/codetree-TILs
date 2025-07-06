start, end = map(int, input().split())

# Please write your code here.
ans = 0
for i in range(start, end + 1):
    divisor_cnt = 0
    for divisor in range(1, i + 1):
        if i % divisor == 0:
            divisor_cnt += 1
    if divisor_cnt == 3:
        ans += 1
print(ans)
MAX_S = 2*10**9

s = int(input())

left = 1
right = MAX_S
max_ = 0

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) //2 <= s:
        left = mid + 1
        max_ = max(max_, mid)
    else:
        right = mid - 1
print(max_)
m = int(input())
a, b = map(int, input().split())

min_cnt = float("INF")
max_cnt = -float("INF")

def bina(target_num):
    left = 1
    right = m
    cnt = 0

    while left <= right:
        cnt += 1
        mid = (left + right) // 2
        if mid == target_num:
            return cnt
        if mid > target_num:
            right = mid - 1
        else:
            left = mid + 1
    return cnt
while a <= b:
    target_num = a
    cnt = bina(target_num)
    a += 1
print(min_cnt, max_cnt)
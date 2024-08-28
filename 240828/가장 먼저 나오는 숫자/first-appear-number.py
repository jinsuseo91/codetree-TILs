n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
querries = list(map(int, input().split()))

def lower_bound(target):
    left, right = 1, n
    min_idx = n + 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    return min_idx

for querry in querries:
    lo = lower_bound(querry)
    if lo <= n and arr[lo] == querry:
        print(lo)
    else:
        print(-1)
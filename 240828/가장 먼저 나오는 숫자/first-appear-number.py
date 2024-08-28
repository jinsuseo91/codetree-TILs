n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))

def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

for i in arr1:
    lo = lower_bound(i)
    if lo <= n and arr[lo] == i:
        print(lo + 1)
    else:
        print(-1)
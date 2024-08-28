n, m = map(int, input().split())
arr = list(map(int, input().split()))

def upper_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    return min_idx

def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    return min_idx

arr.sort()

for _ in range(m):
    a, b = map(int, input().split())
    count = upper_bound(b) - lower_bound(a)
    print(count)
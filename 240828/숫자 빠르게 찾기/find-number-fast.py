n, m = map(int, input().split())

arr = list(map(int, input().split()))

def find(target):
    left, right = 0, n - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

for _ in range(m):
    x = int(input())
    index = find(x)
    print(-1 if index < 0 else index + 1)
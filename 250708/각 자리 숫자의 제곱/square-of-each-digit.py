arr = list(input())
n = len(arr)

def func(arr, i):
    if i == n:
        return 0

    return func(arr, i + 1) + int(arr[i])**2
print(func(arr, 0))
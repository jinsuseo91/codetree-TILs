n = int(input())

def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return func(n//3) + func(n - 1)
print(func(n))
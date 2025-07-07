n = int(input())

# Please write your code here.
def func(n):
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += i
    return sum_ // 10
print(func(n))
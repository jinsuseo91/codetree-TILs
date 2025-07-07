n = int(input())

# Please write your code here.
def func(n):
    return n % 2 == 0 and (n // 10 + (n % 10)) % 5 == 0

if func(n):
    print("Yes")
else:
    print("No")
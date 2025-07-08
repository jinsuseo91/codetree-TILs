n = int(input())

def num(n):
    if n == 0:
        return
    num(n - 1)
    print(n, end = ' ')
def num2(n):
    if n == 0:
        return
    print(n, end=' ')
    num2(n-1)
num(n)
print()
num2(n)
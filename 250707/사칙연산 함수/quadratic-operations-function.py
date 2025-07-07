a, o, c = input().split()
a = int(a)
c = int(c)
arr = ['+', '-', '/', '*']
# Please write your code here.
def func(a, c, o):
    if o not in arr:
        return False
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '*':
        return a * c
    elif o == '/':
        return a // c

print(a, o, c, "=", func(a, c, o))
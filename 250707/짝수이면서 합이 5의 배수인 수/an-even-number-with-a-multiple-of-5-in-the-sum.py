n = int(input())

# Please write your code here.
def func(n):
    n = str(n)
    n1, n2 = n[0], n[1]
    n1, n2 = int(n1), int(n2)
    n = int(n)
    if n % 2 == 0 and (n1 + n2) % 5 == 0:
        return 'Yes'
    else:
        return"No"
print(func(n))
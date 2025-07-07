n, m = map(int, input().split())

# Please write your code here.
def find(n, m):
    gcd = n * m
    for i in range(gcd, 0, -1):
        if i % n == 0 and i % m == 0:
            gcd = min(gcd, i)
    print(gcd)
find(n, m)

n = int(input())

def hello(n):
    if n == 0:
        return
    n -= 1
    print("HelloWorld")
    hello(n)
hello(n)
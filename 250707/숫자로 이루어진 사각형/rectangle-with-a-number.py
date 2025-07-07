n = int(input())

# Please write your code here.
def string(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if num == 10:
                num = 1
            print(num, end=' ')
            num += 1
        print()
string(n)
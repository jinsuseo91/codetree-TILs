n = int(input())
sum_ = 0
for i in range(1, 101):
    sum_ += i
    if sum_ >= n:
        print(i)
        break
n = int(input())
arr = list(map(int, input().split()))

max_ = 0
min_price = arr[0]

for i in range(n):
    profit = arr[i] - min_price

    if profit > max_:
        max_ = profit

    if min_price > arr[i]:
        min_price = arr[i]

print(max_)
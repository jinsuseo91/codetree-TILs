n = int(input())

arr = list(map(int, input().split()))

max_ = -float('inf')
curr_sum = 0
for i in range(n):
    curr_sum += arr[i]
    if curr_sum > max_:
        max_ = curr_sum    
    if curr_sum < 0:
        curr_sum = 0

print(max_)
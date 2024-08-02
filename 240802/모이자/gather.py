n = int(input())
arr = list(map(int, input().split()))

min_sum = 10000000
sum_ = 0
#n은 방문할 집 번호
for i in range(n):
    sum_ = 0
    #k는 이동하는 집의 인덱스
    for k in range(n):
        sum_ += arr[k] * abs(i - k)
    min_sum = min(min_sum, sum_)

print(min_sum)
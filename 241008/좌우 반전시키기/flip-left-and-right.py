n = int(input())
arr = list(map(int, input().split()))

result = 0

# 두 번째 위치부터 마지막 위치 직전까지 검사
for i in range(1, n):
    # 현재 위치가 0이라면, 이 위치를 눌러야 합니다.
    if arr[i - 1] == 0:
        result += 1
        # 현재 위치와 그 다음 위치를 반전
        arr[i - 1] = 1 - arr[i - 1]
        if i < n:
            arr[i] = 1 - arr[i]

# 모든 값이 1인지 확인
if all(arr):
    print(result)
else:
    print(-1)
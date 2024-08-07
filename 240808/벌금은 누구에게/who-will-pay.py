n, m, k = map(int, input().split())

arr = [int(input()) for _ in range(m)]

penalty_num = [0] * (n + 1)

ans = -1

for i in arr:
    # i번 친구는 벌점 1점 추가
    penalty_num[i] += 1
    # 만약 i번 친구의 벌점이 k이상이면
    if penalty_num[i] >= k:
        # 벌금 당첨
        ans = i
        break
print(ans)
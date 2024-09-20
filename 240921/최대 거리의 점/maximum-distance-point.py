n, m = map(int, input().split())  # n개의 점과 m개의 물건
points = [int(input()) for _ in range(n)]  # 각 점의 좌표 입력받기

# 점을 오름차순으로 정렬
points.sort()

# 두 물건 사이의 최소 거리를 d로 하여 m개의 물건을 설치할 수 있는지 확인하는 함수
def can_place_with_distance(d):
    count = 1  # 첫 번째 물건은 첫 번째 위치에 놓는다고 가정
    last_position = points[0]
    
    for i in range(1, n):
        if points[i] - last_position >= d:
            count += 1
            last_position = points[i]
        if count >= m:
            return True
    return False

# 이진 탐색
left, right = 1, points[-1] - points[0]  # 최소 간격은 1, 최대 간격은 좌표의 최대 차이
answer = 0

while left <= right:
    mid = (left + right) // 2
    if can_place_with_distance(mid):
        answer = mid
        left = mid + 1  # 더 큰 최소 거리를 찾기 위해
    else:
        right = mid - 1  # 더 작은 최소 거리를 찾기 위해

print(answer)
# 전역 상수 및 세그먼트 트리 초기 설정
MAX_HEIGHT = 1000000
SEG_TREE_SIZE = 4 * MAX_HEIGHT + 5

segTree = [0] * SEG_TREE_SIZE
segIndex = [0] * SEG_TREE_SIZE
dpBuckets = [[] for _ in range(MAX_HEIGHT + 1)]

# 현재 지도 상태를 저장하는 리스트
mountainHeights = []
mountainDP = []

# 세그먼트 트리 업데이트 함수
def updateSegmentTree(node, left, right, height, dpValue):
    if height < left or height > right:
        return
    if left == right:
        segTree[node] = dpValue
        segIndex[node] = height
        return
    mid = (left + right) // 2
    updateSegmentTree(node * 2, left, mid, height, dpValue)
    updateSegmentTree(node * 2 + 1, mid + 1, right, height, dpValue)
    
    if segTree[node * 2] <= segTree[node * 2 + 1]:
        segTree[node] = segTree[node * 2 + 1]
        segIndex[node] = segIndex[node * 2 + 1]
    else:
        segTree[node] = segTree[node * 2]
        segIndex[node] = segIndex[node * 2]

# 세그먼트 트리 쿼리 함수 (최대 DP 값 구하기)
def querySegmentTree(node, left, right, queryLeft, queryRight):
    if right < queryLeft or left > queryRight:
        return 0
    if queryLeft <= left and right <= queryRight:
        return segTree[node]
    mid = (left + right) // 2
    leftQuery = querySegmentTree(node * 2, left, mid, queryLeft, queryRight)
    rightQuery = querySegmentTree(node * 2 + 1, mid + 1, right, queryLeft, queryRight)
    return max(leftQuery, rightQuery)

# 초기 지도를 설정하는 함수
def initializeBoard(n, heights):
    for h in range(1, MAX_HEIGHT + 1):
        dpBuckets[h].append(0)

    for height in heights:
        maxPrevDP = querySegmentTree(1, 1, MAX_HEIGHT, 1, height - 1)
        dpValue = maxPrevDP + 1

        dpBuckets[height].append(dpValue)
        mountainHeights.append(height)
        mountainDP.append(dpValue)
        updateSegmentTree(1, 1, MAX_HEIGHT, height, dpValue)

# 산 하나 추가
def addMountain(height):
    maxPrevDP = querySegmentTree(1, 1, MAX_HEIGHT, 1, height - 1)
    dpValue = maxPrevDP + 1

    dpBuckets[height].append(dpValue)
    mountainHeights.append(height)
    mountainDP.append(dpValue)
    updateSegmentTree(1, 1, MAX_HEIGHT, height, dpValue)

# 산 하나 제거
def removeLastMountain():
    height = mountainHeights.pop()
    mountainDP.pop()
    dpBuckets[height].pop()
    newDpValue = dpBuckets[height][-1]
    updateSegmentTree(1, 1, MAX_HEIGHT, height, newDpValue)

# 등산 시뮬레이션 점수 계산 및 출력
def simulateHiking(m_index):
    beforeCableCarDP = mountainDP[m_index - 1] - 1
    afterCableCarDP = segTree[1]
    highestMountain = segIndex[1]
    score = 1000000 * (beforeCableCarDP + afterCableCarDP) + highestMountain
    print(score)

# 입력 처리 및 명령 실행
numQueries = int(input())
for _ in range(numQueries):
    query = list(map(int, input().split()))
    command = query[0]

    if command == 100:
        n = query[1]
        heights = query[2:]
        initializeBoard(n, heights)
    elif command == 200:
        height = query[1]
        addMountain(height)
    elif command == 300:
        removeLastMountain()
    elif command == 400:
        m_index = query[1]
        simulateHiking(m_index)

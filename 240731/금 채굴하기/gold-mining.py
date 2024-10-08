n, m = map(int, input().split())
array = [ list(map(int, input().split())) for _ in range(n)]

# 주어진 k에 대하여 마름모의 넓이를 반환합니다.
def get_area(k):
    return k * k + (k + 1) * (k + 1)

# 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
def get_num_of_gold(row, col, k):
    return sum([
        array[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row - i) + abs(col - j) <= k
    ])

max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(2*(n-1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)
                     
            # 손해를 보지 않으면서 채굴할 수 있는 최대 금의 개수를 저장합니다.
            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)   

print(max_gold)
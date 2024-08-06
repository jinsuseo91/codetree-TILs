from itertools import combinations
# 점 m개를 적절히 선택하여 가장 먼 두 점 사이의 거리가 최소가 되었을 때

def dist_(x1,y1,x2,y2):
    return ((x1-x2) ** 2 + (y1 - y2) ** 2) 

# 그때의 최소 거리에 제곱한 값을 출력합니다

n,m = map(int,input().split())

# m 개 선택

# m 개 중 2 개 선택

point_set = []

for _ in range(n):
    x,y = map(int,input().split())
    point_set.append((x,y))

m_set = list(combinations(point_set,m))

min_val = float('inf')


for points in m_set:
    max_val = -float('inf')
    two_point = list(combinations(points,2))
    for i in two_point:
        check_dist = dist_(i[0][0],i[0][1],i[1][0],i[1][1])
        max_val = max(max_val,check_dist)
    
    min_val = min(max_val,min_val)
        

print(int(min_val))
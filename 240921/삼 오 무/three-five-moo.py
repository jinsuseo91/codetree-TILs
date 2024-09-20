n = int(input())
min_ = int(1e10)
left, right = 1, min_

def is_possible(k):
    tot = k//3 + k//5 + k//15
    return k - tot
    
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid) >= n:
        right = mid - 1
        min_ = min(min_, mid)
    else:
        left = mid + 1
print(min_)
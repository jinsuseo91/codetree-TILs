n, m = map(int, input().split())

arr = list(map(int, input().split()))
ans = []
max_ = 0
memo = {}

def calc():
    sum_ = 0
    for i in ans:
        sum_ ^= i
    return sum_

def choose(curr_num, idx):
    global max_

    # key = tuple(ans)
    # if key in memo:
    #     return memo[key]

    if curr_num == m + 1:
        result = calc()
        max_ = max(max_, result)
        return

    for i in range(idx + 1, n):
        ans.append(arr[i])
        choose(curr_num + 1, i)
        ans.pop()

choose(1, -1)
print(max_)
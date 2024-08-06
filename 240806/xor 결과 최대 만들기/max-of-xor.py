n, m = map(int, input().split())

arr = list(map(int, input().split()))
ans = []
max_ = 0

def calc():
    i, j, k = ans[0], ans[1], ans[2]
    return i^j^k


def choose(curr_num):
    global max_
    if curr_num == m + 1:
        result = calc()
        max_ = max(max_, result)
        return

    for i in arr:
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()
choose(1)
print(max_)
import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited =[False] * (n+1)
numbers = []
min_numbers = []
min_numbers2 = []

ans = -1
def find_max(row) :
    global ans
    global min_numbers, min_numbers2
    if row == n :
        tmp_list = []
        for i in range(n):
            tmp_list.append(arr[numbers[i]][i])
        tmp_ans = ans

        ans = max(ans, sum(tmp_list))

        # min 값 갱신될 때마다 min_numbers 리스트도 갱신
        if tmp_ans != ans :
            min_numbers = tmp_list[:]
    
        # 원소는 다른데 합이 같은 경우 고려
        if ans == sum(tmp_list) :
            min_numbers2 = tmp_list[:]
        return

    for i in range(n):
        if visited[i] == True : continue
        numbers.append(i)
        visited[i] = True
        find_max(row+1)
        numbers.pop()
        visited[i] = False

find_max(0)
min_numbers.sort(); min_numbers2.sort()
print(max(min_numbers[0], min_numbers2[0]))
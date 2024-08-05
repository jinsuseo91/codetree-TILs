n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

#ㄴ자에서 최대값 구하기
def left():
    result = 0
    for i in range(n - 1):
        for j in range(m - 1):
            for k in range(4):
                if k == 0:
                    tro1 = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
                    result = max(result, tro1)
                elif k == 1:
                    tro1 = arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
                    result = max(result, tro1)
                elif k == 2:
                    tro1 = arr[i][j] + arr[i+1][j] + arr[i][j+1]
                    result = max(result, tro1)
                elif k == 3:
                    tro1 = arr[i][j] + arr[i+1][j+1] + arr[i][j+1]
                    result = max(result, tro1)
    return result

def right1():
    result = 0
    for i in range(n):
        for j in range(m - 2):
            tro = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            result = max(result, tro)
    return result

def right2():
    result = 0
    for j in range(m):
        for i in range(n-2):
            tro = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            result = max(result, tro)
    return result
    
result = max(left(), right1(), right2())
print(result)
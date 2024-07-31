n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

#ㄴ자 모양에서 최대값구하기
def left():
    result1 = 0
    for i in range(n-1):
        for j in range(m-1):
            for k in range(4):
                if k == 0:
                    tro1 = array[i][j] + array[i+1][j] + array[i+1][j+1]
                    result1 = max(result1, tro1)
                elif k == 1:
                    tro1 = array[i][j+1] + array[i+1][j] + array[i+1][j+1]
                    result1 = max(result1, tro1)
                elif k == 2:
                    tro1 = array[i][j] + array[i+1][j] + array[i][j+1]
                    result1 = max(result1, tro1)
                elif k == 3:
                    tro1 = array[i][j] + array[i+1][j+1] + array[i][j+1]
                    result1 = max(result1, tro1)
    return result1
#세로 1자 모양에서 최대값 구하기
def right1():
    result2 = 0
    for i in range(n):
        for j in range(m-2):
            tro2 = array[i][j] + array[i][j+1] + array[i][j+2]
            result2 = max(result2, tro2)
    return result2

def right2():
    result3 = 0
    for j in range(m):
        for i in range(n-2):
            tro3 = array[i][j] + array[i+1][j] + array[i+2][j]
            result3 = max(result3, tro3)
    return result3

result = max(left(), right1(), right2())
print(result)
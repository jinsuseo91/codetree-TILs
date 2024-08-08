from sys import stdin
n, m = list(map(int, stdin.readline().split()))
move_A = [list(map(int, stdin.readline().split())) for _ in range(n)]
move_B = [list(map(int, stdin.readline().split())) for _ in range(m)]

cur_A = [0]*1000001
cur_B = [0]*1000001

time_A = 1
for v, t in move_A:
    for _ in range(t):
        cur_A[time_A] = cur_A[time_A-1]+v
        time_A += 1
    
time_B = 1
for v, t in move_B:
    for _ in range(t):
        cur_B[time_B] = cur_B[time_B-1]+v
        time_B += 1
    
#A가 총 이동한 시간과 B가 총 이동한 시간은 항상 동일하게 주어짐을 가정해도 좋습니다.
#이 조건이 없다면 먼저 끝났을 때 마지막 위치를 다른 시간이 끝날 때까지 넣어줘야 함

#가능한 값은 3가지로 A, B, (A,B)임, 상태가 3개이므로 깝치지 말고 상태로 정의하자
cnt = 0
key = 0 #-1, 0, 1상태, 처음은 같은 상태
prev_key = -2
for i in range(1, time_A): #time_A는 1이 증가된 상태임
    if cur_A[i] > cur_B[i]: #순위가 바뀜!
        key = -1
    elif cur_A[i] == cur_B[i]:
        key = 0
    else:
        key = 1

    # 이전 값과 다를 때만 cnt 증가
    if key != prev_key:
        cnt += 1

    # prev값 갱신    
    prev_key = key

print(cnt)
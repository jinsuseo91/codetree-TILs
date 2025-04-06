import sys
input = sys.stdin.readline

q = int(input())
mountains = []

def climb(start, heights):
    score = 0
    now = start
    while True:
        moved = True
        for next in range(now + 1, len(heights)):
            if heights[next] > heights[now]:
                score += 1000000
                now = next
                moved = True
                break
        if not moved:
            break
    return score

for _ in range(q):
    command = input().split()

    if command[0] == 100:
        mountains = list(map(int, command[1:]))

    elif command[0] == 200:
        h = int(command[1])
        mountains.append(h)

    elif command[0] == 300:
        mountains.pop()

    elif command[0] == 400:
        m_index = int(command[1]) - 1
        
        score1 = climb(m_index, mountains)

        score2 = 0
        for teleport in range(m_index + 1, len(mountains)):
            if mountains[teleport] >= mountains[m_index]:
                score2 = 1000000 + climb(teleport, mountains)
                break
        print(max(score1, score2))
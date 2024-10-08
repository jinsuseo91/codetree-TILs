n = int(input())
arr = list(input())
answer = list(input())
result = 0

for i in range(n):
    if arr[i] != answer[i] and (i == 0 or arr[i-1] == answer[i-1]):
        result += 1

print(result)
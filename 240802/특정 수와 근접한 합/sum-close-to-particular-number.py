S, N = map(int, input().split())

numbers = list(map(int, input().split()))

min_result = sum(numbers)

for i in range(S) :
    for j in range(i+1, S-1) :
        number = list(numbers)
        del number[i]
        del number[j]
        plus = 0
        for k in range(len(number)) :
            plus += number[k]
        re = abs(N - plus)
        min_result = min(min_result, re)

print(min_result)
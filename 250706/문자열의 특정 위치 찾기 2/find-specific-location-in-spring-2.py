arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']

a = input()
cnt = 0

for i in range(5):
    if arr[i][2] == a or arr[i][3] == a:
        print(arr[i])
        cnt += 1
print(cnt)
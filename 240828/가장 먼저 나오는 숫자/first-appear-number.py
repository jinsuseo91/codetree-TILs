# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr1 = list(map(int, input().split()))

# def lower_bound(target):
#     left, right = 0, n - 1
#     min_idx = n
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] >= target:
#             min_idx = min(min_idx, mid)
#             right = mid - 1
#         else:
#             left = mid + 1
#     return min_idx

# for i in arr1:
#     if i not in arr:
#         print(-1)
#     else:
#         x = lower_bound(i)
#         print(x+1)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))

# 각 숫자의 첫 번째 등장 위치를 기록하는 딕셔너리
position_map = {}
for idx, num in enumerate(arr):
    if num not in position_map:
        position_map[num] = idx + 1  # 1-based index

# 각 질문에 대해 답변
for x in arr1:
    print(position_map.get(x, -1))
# n = int(input())
# a = []
# b = [int(input()) for _ in range(n)]
# a = [
#     i 
#     for i in range(1, 2*n + 1)
#     if i not in b
# ]

# a.sort()
# b.sort()

# ans = 0
# b_idx = 0
# for a_idx in range(n):
#     if b_idx < n and a[a_idx] > b[b_idx]:
#         ans += 1
#         b_idx += 1
# print(ans)
# 변수 선언 및 입력:
n = int(input())
a_cards = []
b_cards = [
    int(input())
    for _ in range(n)
]
# b 카드 숫자로 이루어진 hashset을 완성해줍니다.
b_set = set(b_cards)

# a 카드를 완성해줍니다.
a_cards = [
    num
    for num in range(1, 2 * n + 1)
    if num not in b_set
]

# a, b 카드 목록을 전부 오름차순으로 정렬해줍니다.
a_cards.sort()
b_cards.sort()

# a의 카드를 작은 숫자부터 보며
# b카드의 앞에서부터 이길 수 있는 순간에 둘을 매칭하는게 최선임을 이용합니다.
ans = 0
b_idx = 0
for a_idx in range(n):
    # a가 현재 b 카드보다 우세하다면
    # 둘을 매칭해주는게 항상 유리합니다.
    if b_idx < n and a_cards[a_idx] > b_cards[b_idx]:
        ans += 1
        b_idx += 1

print(ans)
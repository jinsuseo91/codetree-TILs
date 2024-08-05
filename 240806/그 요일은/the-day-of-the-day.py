# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
day = input()

# 각 달의 일수
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 시작 요일을 Monday로 설정하여 요일 목록 생성
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 전체 일수를 계산하는 함수
def calculate_days(m1, d1, m2, d2):
    days = 0
    if m1 == m2:
        days = d2 - d1 + 1
    else:
        days += num_of_days[m1] - d1 + 1
        for i in range(m1 + 1, m2):
            days += num_of_days[i]
        days += d2
    return days

# 전체 일수 계산
total_days = calculate_days(m1, d1, m2, d2)

# 시작 요일의 인덱스 찾기
start_day_index = day_list.index(day)

# 첫 번째 날짜가 시작 요일 기준으로 몇 번째 요일인지 계산
start_day_offset = (start_day_index - (d1 % 7) + 7) % 7

# 첫 번째 요일에 해당하는 날짜 계산
first_occurrence_day = (7 - start_day_offset) % 7

# 특정 요일이 범위 내에 몇 번 등장하는지 계산
day_count = (total_days - first_occurrence_day + 6) // 7

# 결과 출력
print(day_count)
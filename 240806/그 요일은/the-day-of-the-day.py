# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
day = input()

# 각 달의 일수 (2024년은 윤년이므로 2월이 29일까지 있습니다)
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일 리스트
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 시작 요일이 Monday로 설정된 2024년 1월 1일부터의 누적 일수를 계산하는 함수
def days_from_start_of_year(month, day):
    total_days = sum(num_of_days[:month]) + day
    return total_days

# 입력된 날짜 범위의 시작과 끝 일수를 계산
start_days = days_from_start_of_year(m1, d1)
end_days = days_from_start_of_year(m2, d2)

# 시작 날짜의 요일 인덱스를 계산
start_day_index = (start_days - 1) % 7  # 2024년 1월 1일은 Monday

# 특정 요일의 인덱스를 찾기
target_day_index = day_list.index(day)

# 특정 요일이 범위 내에 몇 번 등장하는지 계산
count = 0
for day_count in range(start_days, end_days + 1):
    if (day_count - 1) % 7 == target_day_index:
        count += 1

# 결과 출력
print(count)
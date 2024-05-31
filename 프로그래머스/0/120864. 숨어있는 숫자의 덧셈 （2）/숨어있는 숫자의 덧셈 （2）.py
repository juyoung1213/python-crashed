def solution(my_string):
    current_num = ''  # 현재 자연수를 저장할 변수
    total_sum = 0  # 자연수들의 합을 저장할 변수
    for char in my_string:
        if char.isdigit():  # 현재 문자가 숫자인지 확인
            current_num += char  # 현재 자연수에 추가
        elif current_num:  # 현재 자연수가 비어있지 않으면
            total_sum += int(current_num)  # 현재 자연수를 정수로 변환하여 합에 추가
            current_num = ''  # 현재 자연수 초기화
    # 마지막 자연수 처리
    if current_num:
        total_sum += int(current_num)
    return total_sum

# 예제 사용
print(solution("ab12cd34ef56"))  # 12 + 34 + 56 = 102
print(solution("a1b2c3d4e5"))    # 1 + 2 + 3 + 4 + 5 = 15

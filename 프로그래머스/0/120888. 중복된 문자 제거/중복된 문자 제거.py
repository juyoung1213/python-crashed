def solution(my_string):
    seen = set()  # 중복 여부를 확인하기 위한 집합
    result = []  # 결과를 담을 리스트

    for char in my_string:
        if char not in seen:
            seen.add(char)  # 새로운 문자를 집합에 추가
            result.append(char)  # 결과 리스트에 추가

    return ''.join(result)  # 리스트를 문자열로 변환하여 반환

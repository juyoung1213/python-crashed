from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0
    
def solution(numbers):
    #숫자 리스트를 문자열 리스트로 변환
    str_numbers = list(map(str, numbers))
    #커스텀 정렬 기준을 사용해서 정렬
    str_numbers.sort(key=cmp_to_key(compare))
    #정렬된 문자열을 이어 붙여 결과 생성
    result = ''.join(str_numbers)
    #결과가 '0'으로 시작하면 '0'을 반환
    return result if result[0] != '0' else '0'
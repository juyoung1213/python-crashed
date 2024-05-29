def solution(age):
    # 숫자와 알파벳을 매핑하는 문자열
    digits_to_chars = 'abcdefghij'
    
    # age를 문자열로 변환
    age_str = str(age)
    
    # 각 숫자를 대응하는 알파벳으로 변환
    result = ''.join(digits_to_chars[int(digit)] for digit in age_str)
    
    return result

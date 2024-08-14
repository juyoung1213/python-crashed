def solution(my_string, index_list):
    # 추출괸 문자들을 저장할 빈 문자열을 생성하기
    result = ''
    
    # index_list의 각 인덱스에 대해 반복하기
    for index in index_list:
        # my_string에서 해당 인덱스의 문자를 가져와서 결과 문자열에 추가하기
        result += my_string[index]
        
    # 최종 결과 문자열에 반환하기
    return result
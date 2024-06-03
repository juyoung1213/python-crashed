def solution(my_string):
    # 빈 세트 만든 후
    # 세트에 알파벳이 없을 경우에는 세트와 정답에 알파벳 추가
    seen = set()
    result = ""
    
    for chr in my_string:
        if chr not in seen:
            seen.add(chr)
            result += chr
    return result
        
    
def solution(my_string):
    answer = ''
    set_letters = set(my_string)
    for chr in my_string:
        if chr in set_letters:
            answer += chr
            set_letters.remove(chr)
    return answer
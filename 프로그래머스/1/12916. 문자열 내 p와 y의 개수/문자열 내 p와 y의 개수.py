"""def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True"""

def solution(s):
    s = s.lower()
    
    count_p = s.count('p')
    count_y = s.count('y')
    
    return count_p == count_y
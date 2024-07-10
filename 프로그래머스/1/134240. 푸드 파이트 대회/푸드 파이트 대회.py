def solution(food):
    # 'left_side' 문자열을 빈 문자열로 초기화
    left_side=""
    
    # 1번 음식부터 차례로 배치를 계산함.
    for i in range(1, len(food)):
        # 해당 음식의 사용 가능한 양을 계산(2로 나눈 몫)
        count = food[i] // 2
        # 왼쪽 부분에 음식을 추가함.
        left_side += str(i) * count
        
    # 왼쪽 부분과 그 반대 순서의 오른쪽 부분을 결합하고, 중앙에 물을 추가함.
    right_side = left_side[::-1] # 오른쪽 부분은 왼쪽 부분의 반대 순서
    result = left_side + "0" + right_side
    
    return result
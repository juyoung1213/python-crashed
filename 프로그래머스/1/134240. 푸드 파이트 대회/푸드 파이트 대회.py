def solution(food):
    left_side="" # 왼쪽 부분을 저장할 변수 초기화
    
    #각 음식 종류에 대해 반복함(1번 음식부터 시작)
    for i in range(1, len(food)):
        count = food[i] // 2 # 사용할 수 있는 음식 양(2로 나눈 몫)
        
        # 해당 음식의 양이 1 이상이면
        if count > 0:
            left_side += str(i) * count # 왼쪽 부분에 추가
            
    right_side = left_side[::-1] # 오른쪽 부분은 왼쪽 부분의 반대 순서
    result = left_side + "0" + right_side # 최종 결과 문자열
    
    return result
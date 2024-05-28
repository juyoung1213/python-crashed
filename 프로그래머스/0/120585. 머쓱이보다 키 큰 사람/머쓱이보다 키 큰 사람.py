def solution(array, height):

    # 머쓱이보다 키가 큰 친구들의 수를 세기 위한 변수 초기화
    count = 0
    
    # 배열을 순회하며 머쓱이보다 키가 큰 친구들을 세기
    for h in array:
        if h > height:
            count += 1
    
    return count

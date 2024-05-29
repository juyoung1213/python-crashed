def solution(num, k):
    # num을 문자열로 변환
    num_str = str(num)
    # k를 문자열로 변환
    k_str = str(k)
    
    # k가 num에 포함되어 있는지 확인
    if k_str in num_str:
        # 포함되어 있다면, k가 처음으로 나타나는 위치의 인덱스를 구함
        return num_str.index(k_str) + 1
    else:
        # 포함되어 있지 않다면 -1을 반환
        return -1

def solution(n):
    # 1부터 n까지의 숫자 중 홀수만 리스트에 담아 반환
    return [i for i in range(1, n + 1) if i % 2 != 0]

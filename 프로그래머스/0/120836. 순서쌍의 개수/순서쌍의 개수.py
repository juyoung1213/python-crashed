def solution(n):
    return len ([i for i in range(n+1) if n%(i+1)==0])
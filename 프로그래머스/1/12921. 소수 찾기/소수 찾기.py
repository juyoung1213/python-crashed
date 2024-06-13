def solution(n):
    prime_set = set(range(2,n+1))

    for num in range(2,n+1):
        prime_set -= set(range(num*2,n+1,num))
    
    return len(prime_set)
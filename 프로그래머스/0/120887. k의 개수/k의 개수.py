def solution(i, j, k):
    k = str(k)
    count = 0
    
    for num in range(i, j + 1):
        num_str = str(num)
        count += num_str.count(k)
    return count
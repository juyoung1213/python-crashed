def solution(answers):
    # 각 수포자의 찍기 패턴
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            s[0] += 1
        if answers[i] == b[i % len(b)]:
            s[1] += 1
        if answers[i] == c[i % len(c)]:
            s[2] += 1
    
    max_score = max(s)
    
    result = [i + 1 for i, score in enumerate(s) if score == max_score]
    
    return result
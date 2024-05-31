def solution(s):
    sorted_chars = sorted(s, key=lambda x: (x.islower(), x), reverse=True)
    return ''.join(sorted_chars)
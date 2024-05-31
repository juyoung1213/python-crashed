"""def solution(before, after):
    if len(before) != len(after):
        return 0
    
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0"""


def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0
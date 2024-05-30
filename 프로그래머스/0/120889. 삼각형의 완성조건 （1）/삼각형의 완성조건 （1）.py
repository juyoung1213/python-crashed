def solution(sides):
    sides.sort()
    return 2 if sides[0]+sides[1]<=sides[2] else 1
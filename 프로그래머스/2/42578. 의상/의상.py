"""from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    
    for name, category in clothes:
        clothes_dict[category] += 1
    
    result = 1
    for count in clothes_dict.values():
        result *= (count + 1)
    
    return result - 1"""

def solution(clothes):
    clothes_map = {}
    for _, ctg in clothes:
        if ctg in clothes_map:
            clothes_map[ctg] += 1 # {"eyewear" = 1} -> {"eyewear" = 2}
        else:
            clothes_map[ctg] = 1
    answer = 1
    
    for ctg in clothes_map:
        answer *= (clothes_map[ctg] + 1)
    return answer - 1
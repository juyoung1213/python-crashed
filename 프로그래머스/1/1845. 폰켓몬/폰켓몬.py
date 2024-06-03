"""def solution(nums):
    unique_pokemon = set(nums)
    
    max_pokemon = len(nums) // 2
    
    return min(len(unique_pokemon), max_pokemon)"""

def solution(nums):
    my_dict = {}
    for num in nums:
        if num not in my_dict:
            my_dict[num] = True
    if len(my_dict) >= len(nums) // 2:
        return len(nums) // 2
    else:
        return len(my_dict)
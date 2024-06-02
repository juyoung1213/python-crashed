def solution(nums):
    unique_pokemon = set(nums)
    
    max_pokemon = len(nums) // 2
    
    return min(len(unique_pokemon), max_pokemon)


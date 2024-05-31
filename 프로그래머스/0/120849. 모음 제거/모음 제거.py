def solution(my_string):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in my_string:
        if char not in vowels:
            result += char
    return result
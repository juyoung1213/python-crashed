def solution(numbers, direction):
    if direction == "left":
        # 첫 번째 요소를 제거하고 끝에 추가
        first_element = numbers.pop(0)
        numbers.append(first_element)
    elif direction == "right":
        # 마지막 요소를 제거하고 앞에 추가
        last_element = numbers.pop()
        numbers.insert(0, last_element)
    return numbers

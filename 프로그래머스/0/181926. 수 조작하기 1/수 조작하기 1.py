def solution(n, control):
    for char in control:
        if char == 'w':
            n += 1
        elif char == 's':
            n -= 1
        elif char == 'd':
            n += 10
        elif char == 'a':
            n -= 10
    return n

# 테스트 케이스
print(solution(0, "wsdawsdassw"))  # Expected output: -1
print(solution(10, "wwww"))        # Expected output: 14
print(solution(5, "sda"))          # Expected output: 4

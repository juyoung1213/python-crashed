def solution(keyinput, board):
    # 캐릭터의 초기 위치
    x, y = 0, 0
    
    # 맵의 경계 계산
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    # 방향키 입력 처리
    for direction in keyinput:
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        
        # 경계를 벗어나지 않도록 조정
        if x > x_limit:
            x = x_limit
        elif x < -x_limit:
            x = -x_limit
        
        if y > y_limit:
            y = y_limit
        elif y < -y_limit:
            y = -y_limit
    
    return [x, y]

# 테스트 케이스
print(solution(["up", "up", "left", "left", "right", "right", "down", "down"], [5, 5]))  # Expected output: [0, 0]
print(solution(["up", "up", "up"], [3, 3]))  # Expected output: [0, 1]
print(solution(["right", "right", "right", "right"], [7, 3]))  # Expected output: [3, 0]


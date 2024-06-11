def solution(numbers, target):
    def dfs(index, current_sum):
        # 기저 조건: 모든 숫자를 다 사용한 경우
        if index == len(numbers):
            # 현재 합계가 타겟과 같다면 1을 반환
            if current_sum == target:
                return 1
            else:
                return 0
        
        # 현재 숫자를 더하는 경우와 빼는 경우의 결과를 합산
        add_case = dfs(index + 1, current_sum + numbers[index])
        subtract_case = dfs(index + 1, current_sum - numbers[index])
        
        # 두 경우의 결과를 합산하여 반환
        return add_case + subtract_case
    
    # DFS 탐색 시작
    return dfs(0, 0)

# 테스트
print(solution([1, 1, 1, 1, 1], 3))  # 출력: 5

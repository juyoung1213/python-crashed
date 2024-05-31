"""def solution(arr1, arr2):
    answer = [[]]
    for A, B in zip[arr1, arr2]:
        #([1,2], [3,4])([2,3], [5,6])
        for a, b in zip(A, b):
            #([1,2], [3,4]) ([2,5], [5,6])"""

def solution(arr1, arr2):
    # 두 행렬의 각 요소를 더하여 새로운 행렬을 반환
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

# 예제
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))
# 출력: [[4, 6], [7, 9]]

            
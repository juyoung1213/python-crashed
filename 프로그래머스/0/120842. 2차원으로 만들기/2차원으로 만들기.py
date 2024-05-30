def solution(num_list, n):
    # 결과를 저장할 빈 리스트 생성
    result = []
    # num_list를 n개씩 잘라서 새로운 리스트에 추가
    for i in range(0, len(num_list), n):
        result.append(num_list[i:i + n])
    return result
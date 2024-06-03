def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list} # {신고 당한 사람 : 횟수}
    
    for r in set(report):
        # 신고 당한 사람 카운트
        reports[r.split()[1]] += 1
    
    for r in set(report):
    # 신고된 모든 경우 중 신고 k번 이상일 경우 정지 처리
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer
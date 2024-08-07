def solution(money):
    # 아이스 아메리카노 한 잔의 가격
    pirce_pre_americano = 5500

    # 최대 마실 수 있는 아메리카노 잔 수 계산
    num_americanos = money // pirce_pre_americano

    # 남은 돈 계산
    remaining_money = money % pirce_pre_americano

    # 결과를 배열에 담아 반환
    return [num_americanos, remaining_money]
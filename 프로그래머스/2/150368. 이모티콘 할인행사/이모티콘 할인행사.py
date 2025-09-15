from itertools import product
    # 우선순위
    # 1. 서비스 가입자 수 늘리기
    # 2. 이모티콘 판매액 늘리기
    
    # 사용자 구매 기준
    # 1. 일정 비율 이상 할인하는 이모티콘 구매
    # 2. 이모티콘 구매 비용 합이 가격 이상이면 서비스 가입
def solution(users, emoticons):
    answer = []
    length = len(emoticons)
    percents = (10, 20, 30, 40)
    result = [0, 0]
    
    # 가능한 할인율의 모든 경우의 수
    available = list(product(percents, repeat = length))
    
    for i in available:
        member, price = 0, 0
        for minimum_percent, maximum_price in users:
            user_price = 0
            for item_price, item_percent in zip(emoticons, i):
                if item_percent >= minimum_percent:
                    user_price += item_price * (100 - item_percent) * 0.01
                
            if user_price >= maximum_price:
                member += 1
            else:
                price += user_price

        result = max(result, [member, price])
    
    return result
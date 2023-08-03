from collections import defaultdict, Counter

def solution(topping):
    answer = 0
    counter = Counter(topping)    # 처음에 나에게 모든 토핑이 있다고 가정
    bro = defaultdict(int)    #동생은 0에서 부터 하나씩 넘겨 받음
    
    for t in topping:
        # 해당 t 토핑에 대해 나는 -1, 동생은 +1
        counter[t] -= 1
        bro[t] += 1
        
        # 만약 모든 토핑 다 넘겨줬다면 더 이상 볼 필요 없음
        if counter[t] == 0:
            del counter[t]
        
        # counter와 bro dict의 길이는 종류이므로 같을 때 +1
        if len(counter) == len(bro):
            answer += 1
    return answer
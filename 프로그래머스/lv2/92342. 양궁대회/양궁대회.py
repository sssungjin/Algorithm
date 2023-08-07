from itertools import combinations_with_replacement
# n 크기 최대 10이고 info 의 길이는 11로 고정되어 있으므로 중복 조합으로 모든 경우의 수 확인
def solution(n, info):
    answer = [-1]
    max_gap = -1
    #라이언이 점수의 모든 경우의 수
    for combi in combinations_with_replacement(range(11),n):
        lion_info = [0] * 11
        # 거꾸로 +1 하면서 저장
        for i in combi:
            lion_info[10-i] += 1
        
        apeach_sum, lion_sum = 0, 0
        for j in range(11):
            # 둘다 0이면 0점
            if info[j] == lion_info[j] == 0:
                continue
            # 어피치가 같거나 크면 점수 어피치에 +
            elif info[j] >= lion_info[j]:
                apeach_sum += 10 - j
            # 라이언이 더 크면 라이언 +
            else:
                lion_sum += 10 - j
        
        # 라이언 합이 더 크면
        if lion_sum > apeach_sum:
            gap = lion_sum - apeach_sum
            # 더 큰 차이로 라이언이 이긴 경우 answer 배열에 해당 배열 저장
            if gap > max_gap:
                max_gap = gap
                answer = lion_info
    return answer
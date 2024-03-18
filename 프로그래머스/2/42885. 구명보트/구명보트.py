def solution(people, limit):
    answer = 0
    people.sort()
    s, e = 0, len(people) - 1
    
    while s <= e:
        # 두명 구출
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        # 두명 안된다면 큰 사람 구출
        else:
            e -= 1
        answer += 1
    return answer

# 50 50 70 80
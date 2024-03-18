def solution(s):
    answer = []
    
    # 전처리
    s = s.split("},")
    arr = []
    for i in s:
        arr.append(i.replace("{", "").replace("}", "").split(","))
    arr.sort(key = len)
    
    # 순서대로 정렬했으므로 answer에 순서대로 없는 것을 삽입하면 됨
    for element in arr:
        for i in element:
            if i not in answer:
                answer.append(i)
    
    return list(map(int, answer))
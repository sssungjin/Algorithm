def solution(user_id, banned_id):
    answer = 0
    # id 하나당 모든 배너 id와 비교
    # 같은 문자이거나 *이면 패스하고 만약에 다르면 flag false로 처리
    # flag true인 값을 배열에 넣음
    # fr*d* 에 대한건 frodo, fradi
    # *rodo에 대한건 frodo, crodo
    # ****** abc123, frodoc
    banned_candidates = [[] for _ in range(len(banned_id))]

    for i in range(len(user_id)):
        user = user_id[i]
        for k in range(len(banned_id)):
            flag = True
            banned = banned_id[k]
            if len(user) != len(banned):
                flag = False
                continue
                
            for j in range(len(user)):
                if user[j] != banned[j]:
                    if banned[j] != '*':
                        flag = False
                        break
            if flag == True:
                banned_candidates[k].append(user)
            
    #print(banned_candidates)
    
    banned_length = len(banned_id)
    combinations = set()
    
    def dfs(depth, current_combination):
        if depth == banned_length:
            combinations.add(frozenset(current_combination))
            return
        
        candidates = banned_candidates[depth]
        for user in candidates:
            if user in current_combination:
                continue
            
            current_combination.add(user)
            
            dfs(depth + 1, current_combination)
            
            current_combination.remove(user)
    
    dfs(0, set())
    
    return len(combinations)
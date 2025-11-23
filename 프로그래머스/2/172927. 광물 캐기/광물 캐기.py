def solution(picks, minerals):
    dia_pick, iron_pick, stone_pick = picks[0], picks[1], picks[2]
    total_picks = dia_pick + iron_pick + stone_pick
    
    mineral_arr = []
    answer = 0
    
    max_mineral_index = min(len(minerals), total_picks * 5)
    
    for i in range(0, max_mineral_index, 5):
        segment = minerals[i:i+5] 
        d_count, i_count, s_count = 0, 0, 0
        
        for m in segment:
            if m == "diamond": d_count += 1
            elif m == "iron": i_count += 1
            else: s_count += 1
            
        mineral_arr.append([d_count, i_count, s_count])

    mineral_arr.sort(key=lambda arr: arr[0] * 25 + arr[1] * 5 + arr[2], reverse=True)
    
    for arr in mineral_arr:
        d_count, i_count, s_count = arr[0], arr[1], arr[2]
        
        if dia_pick > 0:
            dia_pick -= 1
            answer += d_count + i_count + s_count
        
        elif iron_pick > 0:
            iron_pick -= 1
            answer += d_count * 5 + i_count * 1 + s_count * 1
            
        elif stone_pick > 0:
            stone_pick -= 1
            answer += d_count * 25 + i_count * 5 + s_count * 1
            
        else:
            break
            
    return answer
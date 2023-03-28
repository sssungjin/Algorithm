def solution(storey):
    answer = 0

    while storey != 0:
        print(storey)
        div = storey % 10
        if div > 5:
            answer += 10 - div
            storey += 10 - div
        elif div == 5:
            if (storey // 10) % 10 >= 5:
                storey += 10 - div
            else:
                storey -= div
            answer += div
        else:
            answer += div
            storey -= div
        print(storey)
        storey //= 10
        
    return answer

#앞자리만 확인해서 0~5면 바로 -, 6~9면 +해서 10으로 맞춘다음에 -10
#6199 -> +1000*4, -10000, -100, +1, -100 
#3825 -> -1000*3, +100*2, -1000, -10*2, -1*5
#       -> +100*2, -1000*4, ...
#2554 -> -1000 * 2, -100 * 5, -10*5, -1*4
#16     -> -10*1, +1*4, -10*1
#99800 -> +100*2, -100000
#91400 -> +10000, -100000, -1000, -100*4
#96700 -> +100*3, -1000*7, +10000, -100000
from itertools import product

def check_distance(place):
    plist = [(x,y) for x in range(5) for y in range(5) if place[x][y] == 'P']
    
    for x1,y1 in plist:
        for x2,y2 in plist:
            distance = abs(x1-x2) + abs(y1-y2)
            if distance == 0 or distance > 2:
                continue
            
            #붙어있는 경우
            if distance == 1:
                return 0
            #같은 행에서 파티션 체크
            elif x1 == x2 and place[x1][int((y1+y2)/2)] != 'X':
                return 0
            #같은 열에서 파티션 체크
            elif y1 == y2 and place[int((x1+x2)/2)][y1] != 'X':
                return 0
            #같은행 같은열 아닐때 파티션 체크(대각선)
            elif y1 != y2 and x1 != x2:
                if place[x2][y1] != 'X' or place[x1][y2] != 'X':
                    return 0
    return 1
def solution(places):
    answer = []
    for place in places:
        answer.append(check_distance(place))
    return answer

# |x1-x2| + |y1-y2|
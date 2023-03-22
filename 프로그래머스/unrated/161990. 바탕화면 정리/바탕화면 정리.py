def solution(wallpaper):
    answer = [51, 51, -1, -1]
    #0: 왼쪽 1: 위 2: 오른쪽 3: 아래
    for y,val in enumerate(wallpaper):
        for x,v in enumerate(wallpaper[y]):
            if v == '#':
                #가장 위쪽 값 찾기(작아야됨)
                if y < answer[0]:
                    answer[0] = y
                #가장 왼쪽 값 찾기(작아야됨)
                if x < answer[1]:
                    answer[1] = x
                #가장 아래쪽 값 찾기(커야됨)
                if y > answer[2]:
                    answer[2] = y
                #가장 오른쪽 값 찾기(커야됨)
                if x > answer[3]:
                    answer[3] = x
    answer[2] += 1
    answer[3] += 1
    return answer

#가장 왼쪽x좌표 + 가장 위(y좌표)
#가장 오른쪽x좌표 + 가장 아래y좌표
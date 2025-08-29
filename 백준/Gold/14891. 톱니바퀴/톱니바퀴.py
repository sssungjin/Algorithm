gear = [(input()) for _ in range(4)]
K = int(input())
command = [list(map(int, input().split())) for _ in range(K)]

def rotate(direction, g_str):

    if direction == 1: # 시계
        return g_str[-1] + g_str[:-1]
    else: # 반시계
        return g_str[1:] + g_str[0]

# gear[i][2], gear[i+1][6]
# gear[i][2], gear[i-1][6]

for num, direction in command:
    num -= 1
    
    rotation_info = [0] * 4
    rotation_info[num] = direction
    
    for i in range(num, 3):
        if gear[i][2] != gear[i + 1][6]:
            rotation_info[i + 1] = -rotation_info[i]
        else:
            break
        
    for i in range(num, 0, -1):
        if gear[i][6] != gear[i -1][2]:
            rotation_info[i - 1] = -rotation_info[i]
        else:
            break
    
    for i in range(4):
        if rotation_info[i] != 0:
            gear[i] = rotate(rotation_info[i], gear[i])


score = 0
if gear[0][0] == '1': # S극이면
    score += 1
if gear[1][0] == '1':
    score += 2
if gear[2][0] == '1':
    score += 4
if gear[3][0] == '1':
    score += 8

print(score)        
        

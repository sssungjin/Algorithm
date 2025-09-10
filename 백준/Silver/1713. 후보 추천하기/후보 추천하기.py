from collections import defaultdict

N = int(input())
M = int(input())
recommend = list(map(int, input().split()))

# key: 학생 번호
# value: [추천 수, 게시 시간]
frame = {}

for i in range(M):
    time = i
    id = recommend[i]
    
    if id in frame:
        frame[id][0] += 1
    
    else:
        if len(frame) < N:
            frame[id] = [1, time]
        else:
            evict_key = min(frame.keys(), key = lambda k: (frame[k][0], frame[k][1]))
            del frame[evict_key]
            frame[id] = [1, time]
            
ans = sorted(list(frame.keys()))

print(*ans)
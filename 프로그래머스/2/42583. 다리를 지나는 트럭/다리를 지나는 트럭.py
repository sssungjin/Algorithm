from collections import deque

# 핵심 아이디어: bridge를 length 크기만큼 0으로 초기화하고 pop하면 차 나간것처럼 처리 가능

def solution(bridge_length, weight, truck_weights):
    time = 0
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    cur_weight = 0
    
    while bridge:
        time += 1
        cur_weight -= bridge.popleft()
        
        if waiting:
            if cur_weight + waiting[0] <= weight:
                truck = waiting.popleft()
                bridge.append(truck)
                cur_weight += truck
            else:
                bridge.append(0)
    
    return time
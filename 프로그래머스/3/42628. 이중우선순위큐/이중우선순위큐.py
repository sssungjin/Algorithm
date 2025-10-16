import heapq
from collections import defaultdict

def solution(operations):
    answer = []
    
    # -1 곱해서 넣기
    max_heap = []
    
    # pop하면 최댓값 삭제
    heapq.heapify(max_heap)
    
    # 기본 heapq는 pop하면 가장 작은 원소 반환 및 삭제
    min_heap = []
    heapq.heapify(min_heap)
    
    is_valid = defaultdict(int)
    
    
    for op in operations:
        command, value_str = op.split()
        value = int(value_str)

        if command == 'I':
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            is_valid[value] += 1
            
        elif command == 'D':
            if value == 1:
                while max_heap and is_valid[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    valid_max_val = -heapq.heappop(max_heap)
                    is_valid[valid_max_val] -= 1
            else:
                while min_heap and is_valid[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    valid_min_val = heapq.heappop(min_heap)
                    is_valid[valid_min_val] -= 1
        
        while max_heap and is_valid[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        
        while min_heap and is_valid[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        
        
    if not max_heap or not min_heap:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]
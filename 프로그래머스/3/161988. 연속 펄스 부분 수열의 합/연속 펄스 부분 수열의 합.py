def pulse_max(arr):
    pulse1 = [-1, 1]
    pulse2 = [1, -1]
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            sum1 += pulse1[0] * arr[i]
        else:
            sum1 += pulse1[1] * arr[i]
    
    for i in range(len(arr)):
        if i % 2 == 0:
            sum2 += pulse2[0] * arr[i]
        else:
            sum2 += pulse2[1] * arr[i]
    
    return max(sum1, sum2)

def solution(sequence):
    answer = 0
    n = len(sequence)
    
    pulsed_seq1 = [0] * n
    pulsed_seq2 = [0] * n
    
    
    pulse = 1
    for i in range(n):
        pulsed_seq1[i] = sequence[i] * pulse
        pulsed_seq2[i] = sequence[i] * -pulse
        pulse *= -1
    
    def get_max_pulse(arr):
        if not arr:
            return 0
        
        max_so_far = arr[0]
        current_max = arr[0]
        
        for i in range(1, len(arr)):
            current_max = max(arr[i], current_max + arr[i])
            
            max_so_far = max(current_max, max_so_far)
            
        return max_so_far
    
    max1 = get_max_pulse(pulsed_seq1)
    max2 = get_max_pulse(pulsed_seq2)
    
    if n == 0:
        return 0
    else:
        return max(max1, max2)
        
        
    return answer
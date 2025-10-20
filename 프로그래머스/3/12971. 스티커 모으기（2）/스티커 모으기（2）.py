def solution(sticker):
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    def get_max_sum(arr):
        length = len(arr)
        
        if length == 0:
            return 0
        if length == 1:
            return arr[0]
        
        dp = [0] * length
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, length):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            
        
        return dp[-1]
    
    max_sum1 = get_max_sum(sticker[:-1])
    
    max_sum2 = get_max_sum(sticker[1:])
            
    return max(max_sum1, max_sum2)
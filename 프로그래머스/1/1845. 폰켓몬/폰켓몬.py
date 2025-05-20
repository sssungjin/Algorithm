from collections import defaultdict

def solution(nums):
    poketmon = defaultdict(int)
    n = len(nums) / 2
    catch = set()    
    
    for i in nums:
        poketmon[i] += 1
        
    for key in poketmon.keys():
        if n > 0 and poketmon[key] > 0:
            poketmon[key] -= 1
            catch.add(key)
            n -= 1
            
    return len(catch)
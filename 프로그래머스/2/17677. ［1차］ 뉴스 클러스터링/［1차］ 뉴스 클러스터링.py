from collections import Counter

def solution(str1, str2):
    answer = 0
    str1_arr, str2_arr = [], []
    
    for i in range(0, len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_arr.append((str1[i]+str1[i+1]).upper())
    
    for i in range(0, len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_arr.append((str2[i]+str2[i+1]).upper())

    counter1 = Counter(str1_arr)
    counter2 = Counter(str2_arr)
    
    intersection = counter1 & counter2
    union = counter1 | counter2
    
    inter_count = sum(intersection.values())
    union_count = sum(union.values())
    
    if union_count == 0:
        return 65536
    
    jacard = inter_count / union_count
    return int(jacard * 65536)
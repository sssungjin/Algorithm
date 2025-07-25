from itertools import combinations
import sys

input = sys.stdin.readline

word = input().strip()
number = [i for i in range(1, len(word))]

length_combi = list(combinations(number, 2))

ans = []

for start, end in length_combi:
    first = word[:start]
    second = word[start:end]
    third = word[end:]
    
    reverse_first = first[::-1]
    reverse_second = second[::-1]
    reverse_third = third[::-1]
    
    full_word = reverse_first + reverse_second + reverse_third
    
    ans.append(full_word)
    
ans.sort()

print(ans[0])
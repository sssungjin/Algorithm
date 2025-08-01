from collections import Counter

name = input()
counter = Counter(name)

mid = ''
half = []

# 홀수 개수인 문자열 1개면 가운데에 배치
# 홀수 개수인 문자열 2개 이상이면 불가능
odd_count = 0
for char, cnt in sorted(counter.items()):
    if cnt % 2 == 1:
        odd_count += 1
        mid = char
        if odd_count > 1:
            print("I'm Sorry Hansoo")
            exit()
    half.append(char * (cnt // 2))

half_str = ''.join(half)
result = half_str + mid + half_str[::-1]
print(result)
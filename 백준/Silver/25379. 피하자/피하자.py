n = int(input())
arr = list(map(int, input().split()))

odd_left = 0
odd_right = 0
even_left = 0
even_right = 0

cnt = 0

# 홀수를 왼쪽으로 몰 때
for i in arr:
    if i % 2 == 0:
        cnt += 1
    else:
        odd_left += cnt

cnt = 0

# 홀수를 오른쪽으로 몰 때때
for i in arr[::-1]:
    if i % 2 == 0:
        cnt += 1
    else:
        odd_right += cnt

cnt = 0

# 짝수를 왼쪽으로 몰 때때
for i in arr:
    if i % 2 == 1:
        cnt += 1
    else:
        even_left += cnt

cnt = 0

# 짝수를 오른쪽으로 몰 때
for i in arr[::-1]:
    if i % 2 == 1:
        cnt += 1
    else:
        even_right += cnt
        
print(min(odd_left, odd_right, even_left, even_right))
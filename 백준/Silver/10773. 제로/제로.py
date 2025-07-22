k = int(input())

number = [int(input()) for _ in range(k)]
ans = []

for i in number:
    if i != 0:
        ans.append(i)
    else:
        ans.pop()
    
print(sum(ans))
X = (input())
cnt = 0

while len(X) > 1:
    cnt += 1
    current_sum = 0
    
    for c in X:
        current_sum += int(c)
        
    X = str(current_sum)
    
print(cnt)
if int(X) % 3 == 0:
    print("YES")
else:
    print("NO")
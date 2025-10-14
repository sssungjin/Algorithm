str1 = input()
explosion = input()

stack = []
exp_len = len(explosion)

for char in str1:
    stack.append(char)
    
    if stack[-exp_len:] == list(explosion):
        for _ in range(exp_len):
            stack.pop()

result = "".join(stack)

if not result:
    print("FRULA")
else:
    print(result)
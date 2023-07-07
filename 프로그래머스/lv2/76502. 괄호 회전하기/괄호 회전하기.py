def solution(s):
    answer = 0
    for _ in range(len(s)):
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            answer += 1
        s = s[1:] + s[:1]
            
    return answer
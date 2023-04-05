def solution(ingredient):
    answer = 0
    cook = []
    lst = [1,2]
    for i in ingredient:
        cook.append(i)
        if cook[-4:] == [1,2,3,1]:
            answer += 1
            del cook[-4:]
    return answer

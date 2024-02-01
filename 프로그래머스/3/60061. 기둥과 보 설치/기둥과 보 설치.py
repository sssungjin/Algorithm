def check(answer):
    for x, y, a in answer:
        if a == 0:
            # 기둥 설치
            # 설치 가능한 조건이 없다면 False
            # 바닥인지, 아래에 기둥이 있는지, 오른쪽이나 왼쪽에 보가 있는지
            if (y != 0 and 
                [x, y - 1, 0] not in answer and
                [x - 1, y, 1] not in answer and
                [x, y, 1] not in answer):
                return False
        else:
            # 보 설치
            # 아래에 기둥이 존재하는지, 양쪽 모두에 보가 존재하는지
            if ([x, y - 1, 0] not in answer and 
                [x + 1, y - 1, 0] not in answer and
                ([x - 1, y, 1] not in answer or
                 [x + 1, y, 1] not in answer)):
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            answer.remove([x, y, a])
            # 먼저 삭제하고 check 해서 false라면 재설치 (삭제 취소)
            if not check(answer):
                answer.append([x, y, a])
        elif b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
    answer.sort()
    return answer
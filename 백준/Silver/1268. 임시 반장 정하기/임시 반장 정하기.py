n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

# 각 학생마다 같은 반을 해본 학생이 몇 명인지 저장
counts = [0] * n

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        # i번과 j번이 5년 중 한 번이라도 같은 반이었는지 확인
        for k in range(5):
            if classes[i][k] == classes[j][k]:
                counts[i] += 1
                break  # 한 번이라도 같으면 카운트 후 더 비교 X

# 가장 많이 같은 반을 한 학생 번호 구하기
max_count = max(counts)
for i in range(n):
    if counts[i] == max_count:
        print(i + 1)
        break

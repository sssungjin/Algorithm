from itertools import combinations

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 1. 초기 적 위치는 한 번만 계산 (시뮬레이션에서 복사해서 사용)
initial_enemies = set()
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            initial_enemies.add((r, c))

max_killed_count = 0
archer_placements = combinations(range(M), 3)

for archer_pos in archer_placements:
    # 1. 시뮬레이션 시작 전, 적 위치 초기화
    current_enemies = initial_enemies.copy()
    current_killed_count = 0

    while current_enemies:
        # 각 궁수가 공격할 대상 찾기 (동시 공격이므로 한 번에 모음)
        targets_to_remove = set()
        for archer_c in archer_pos:
            # 공격 가능한 후보 찾기
            candidates = []
            for (r, c) in current_enemies:
                dist = abs(N - r) + abs(archer_c - c)
                if dist <= D:
                    # (거리, 열, 행) 순으로 저장 -> 정렬 편의성
                    candidates.append((dist, c, r))

            # 후보가 있으면 정렬해서 최종 타겟 결정
            if candidates:
                candidates.sort()
                final_target = (candidates[0][2], candidates[0][1])  # (행, 열)
                targets_to_remove.add(final_target)

        # 이번 턴에 잡은 적 수 계산 및 제거
        current_killed_count += len(targets_to_remove)
        current_enemies -= targets_to_remove  # set의 차집합 연산

        # 적 이동 (새로운 set을 만들어 교체)
        next_enemies = set()
        for (r, c) in current_enemies:
            if r + 1 < N:
                next_enemies.add((r + 1, c))
        current_enemies = next_enemies

    max_killed_count = max(max_killed_count, current_killed_count)

print(max_killed_count)
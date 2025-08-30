N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    # 주사위 숫자 총합에서 가장 큰 값을 뺀 것이 5면의 합의 최솟값
    print(sum(dice) - max(dice))
else:
    # 마주보는 면의 인덱스: (0, 5), (1, 4), (2, 3)
    # 각 쌍에서 작은 값들을 골라 놓음
    min_faces = [
        min(dice[0], dice[5]),
        min(dice[1], dice[4]),
        min(dice[2], dice[3])
    ]
    min_faces.sort() # 작은 순으로 정렬

    # 1면, 2면, 3면이 보일 때의 최소 합
    min1 = min_faces[0]
    min2 = min_faces[0] + min_faces[1]
    min3 = min_faces[0] + min_faces[1] + min_faces[2]

    # 각 종류별 면의 개수 계산
    # 3면이 보이는 꼭대기 모서리: 4개
    count3 = 4
    # 2면이 보이는 모서리: 위쪽 4*(N-2) + 옆면 4*(N-1)
    count2 = 4 * (N - 2) + 4 * (N - 1)
    # 1면이 보이는 나머지: 위쪽 (N-2)^2 + 옆면 4*(N-1)*(N-2)
    count1 = (N - 2) * (N - 2) + 4 * (N - 1) * (N - 2)
    
    # 최종 답 계산
    ans = (min3 * count3) + (min2 * count2) + (min1 * count1)
    print(ans)
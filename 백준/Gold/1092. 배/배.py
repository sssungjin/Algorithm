import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

time = 0
cranes.sort(reverse = True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
else:
    while len(boxes) > 0:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        time += 1

    print(time)
from collections import Counter

n = int(input())

for _ in range(n):
    tmp = (list(map(int, input().split())))
    t = tmp[0]
    tmp = tmp[1:]

    count_soldier = Counter(tmp)
    most_common_soldier = count_soldier.most_common(1)
      
    if most_common_soldier[0][1] >  (t // 2):
        print(most_common_soldier[0][0])
    else:
        print('SYJKGW')
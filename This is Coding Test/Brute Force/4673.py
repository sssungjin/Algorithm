# 여러 개의 생성자로 하나의 값을 만들 수 있기 때문에 
# set로 중복 제거
natural = set(range(1, 10001))
number = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
        # 850 + 8
        # 850 + 8 + 5
        # 850 + 8 + 5 + 0
    number.add(i)

# 차집합
self_num = sorted(natural - number)
for i in self_num:
    print(i)
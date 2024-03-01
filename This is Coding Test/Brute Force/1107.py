target = int(input())
n = int(input())
broken = list(map(int, input().split()))

answer = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums) - 1:
            # 길이 = 몇개의 버튼을 눌러서 nums를 입력할 수 있는지
            # 거기에 더하기 nums - target
            answer = min(answer, abs(int(nums) - target) + len(nums))

print(answer)
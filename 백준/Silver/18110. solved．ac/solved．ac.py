from decimal import Decimal, ROUND_HALF_UP
import sys
input = sys.stdin.readline

def custom_round(value):
    return int(Decimal(str(value)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

n = int(input())

if n == 0:
    print(0)
    sys.exit()

opinion = [int(input()) for _ in range(n)]
opinion.sort()

x = custom_round(n * 0.15)

level = opinion[x: n - x] if x > 0 else opinion
avg = sum(level) / len(level)

print(custom_round(avg))
import sys

식 = sys.stdin.readline().strip()

# -로 나눔
splits = 식.split('-')
# 각 나눈 부분의 합들
sums = [sum(map(int, p.split('+'))) for p in splits]
print(sums[0] - sum(sums[1:]))
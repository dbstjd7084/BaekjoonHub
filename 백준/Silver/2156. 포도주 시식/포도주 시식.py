import sys

# 테스트 실행 횟수 입력받기
n = int(sys.stdin.readline())
# 실행 횟수만큼 입력받기
wine = [int(sys.stdin.readline()) for _ in range(n)]

# 합산 시작 지점 0 또는 1임
# 3가지의 경우의 수가 있음
# 앞의 시작 개수가 1 또는 2개고, 1인 경우는 0부터
# 2인 경우에는 "0부터" 와 "1부터"
# 1: 12, 45, 78, ...
# 2: 01, 34, 67, ...
# 3: 0, 23, 56, ...

# wine 목록에서 최적의 수 구하기
if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], (dp[i-3] if i > 2 else 0) + wine[i-1] + wine[i])

    print(dp[-1])
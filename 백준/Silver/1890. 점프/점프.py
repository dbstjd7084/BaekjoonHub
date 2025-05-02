import sys

N = int(sys.stdin.readline())

# 게임판 입력
게임판 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        if 게임판[y][x] == 0 or dp[y][x] == 0:
            continue

        jump = 게임판[y][x]
        if x + jump < N:
            dp[y][x+jump] += dp[y][x]
        if y + jump < N:
            dp[y+jump][x] += dp[y][x]

# 출력
print(dp[N-1][N-1])
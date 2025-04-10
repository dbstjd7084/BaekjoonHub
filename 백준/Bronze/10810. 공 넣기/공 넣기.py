import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())

    for change in range(i, j+1):
        basket[change-1] = k

# 출력력
print(*basket)
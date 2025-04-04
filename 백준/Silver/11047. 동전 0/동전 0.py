import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

ans = 0
for c in coins[::-1]:
    if K == 0:
        break
    ans += K // c
    K %= c

print(ans)
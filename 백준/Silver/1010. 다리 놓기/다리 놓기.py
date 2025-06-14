import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    if N == M:
        print(1)
    elif N == 1:
        print(M)
    else:
        value = M
        for i in range(M-1, M-N, -1):
            value *= i
        for j in range(1, N+1):
            value //= j
        print(value)
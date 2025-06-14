import sys

N = int(sys.stdin.readline())
Pi = list(map(int, sys.stdin.readline().split()))

Pi.sort()

before = 0
min_sum = 0
for i in range(N):
    P = Pi[i]
    Pi[i] += before
    before += P
    min_sum += before

print(min_sum)
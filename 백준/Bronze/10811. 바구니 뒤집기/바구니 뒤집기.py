import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    reverse_basket = basket[i-1:j][::-1]

    basket[i-1:j] = reverse_basket

print(*basket)
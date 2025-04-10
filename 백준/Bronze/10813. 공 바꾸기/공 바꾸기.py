import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    # 두 바구니 안에 든 공 교환환
    trash = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = trash

print(*basket)
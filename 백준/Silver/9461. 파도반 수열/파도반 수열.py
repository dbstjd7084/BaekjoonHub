from sys import stdin

# 파도반 수열 구하기
def P(N):
    P = [1, 1, 1, 2, 2, 3, 4, 5]
    if N <= 8:
        return P[N-1]
    point = 7
    while True:
        if len(P) == N:
            return P[N-1]
        P.append(P[point] + P[point-4])
        point += 1

# 테스트 케이스만큼 입력 반복
for T in range(int(stdin.readline())):
    print(P(int(stdin.readline())))
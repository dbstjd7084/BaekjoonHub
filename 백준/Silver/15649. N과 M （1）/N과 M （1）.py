import sys

N, M = map(int, sys.stdin.readline().split())

M개_수열 = [i+1 for i in range(M)]

def 백트래킹(path):
    # path의 수열 개수가 M개일 때 출력
    if len(path) == M:
        print(*path)
        return
    # 아니라면 포함이 되어있지 않는 요소 추가해 재귀
    for i in range(1, N+1):
        if i not in path:
            백트래킹(path + [i])

백트래킹([])
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N + 1)
path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack()
            path.pop()
            visited[i] = False

backtrack()

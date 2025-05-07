import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

# 미로 입력
미로 = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
def bfs():
    visited = [[-1] * M for _ in range(N)]
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = 0

    dir_y = (-1, 1, 0, 0)
    dir_x = (0, 0, -1, 1)

    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny, nx = y + dir_y[i], x + dir_x[i]
            if 0 <= ny < N and 0 <= nx < M:
                count = visited[y][x] + 미로[ny][nx]
                if visited[ny][nx] == -1 or visited[ny][nx] > count:
                    visited[ny][nx] = count
                    if 미로[ny][nx] == 1:
                        dq.append((ny, nx))
                    else:
                        dq.appendleft((ny, nx))
    return visited[N-1][M-1]

print(bfs())
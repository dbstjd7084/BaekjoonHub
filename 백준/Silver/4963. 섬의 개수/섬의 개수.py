import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 크게 설정

# 8 방향
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
dx = (-1, -1, -1, 0, 0, 1, 1, 1)

# DFS
def dfs (y, x):
    # 방문 표시
    visited[y][x] = True

    # 8 방향으로 깊이 탐색
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < h and 0 <= nx < w):
            continue
        if arr[ny][nx] == 0:
            continue
        if not visited[ny][nx]:
            dfs(ny, nx)

while True:
    w, h = map(int, sys.stdin.readline().split())

    # 종료 조건
    if w == 0 and h == 0:
        break

    # 인접 행렬
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    # 방문 목록 생성
    visited = [[False] * w for _ in range(h)]
    # 섬의 수
    island_count = 0

    # arr 에서 땅들 각각 dfs 실행
    for y in range(h):
        for x in range(w):
            # 모든 1인 땅들 실행하기
            if arr[y][x] == 1:
                if not visited[y][x]:
                    # 섬 추가
                    island_count += 1
                    # 탐색 실행
                    dfs(y, x)

    print(island_count)
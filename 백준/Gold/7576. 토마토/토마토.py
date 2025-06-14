from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque()

# 익은 토마토들 큐에 입력
for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            queue.append((y, x))

# 방향 리스트
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 익은 토마토들 실행
# 이 경우 큐에 아무것도 없을 때까지 돌아가기 때문에
# 계속 추가가 안될 때까지 반복됨
# box는 계속 며칠째에 익었는지 저장하면서 확산
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        # 정해진 범위이고, 그곳에 안 익은 토마토가 있을 경우
        if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1
            queue.append((ny, nx))

days = 0
for row in box:
    for cell in row:
        # 안 익은 토마토가 있는 경우
        if cell == 0:
            print(-1)
            exit()
        # days값과 cell의 확산일 값 중 큰 값 저장
        days = max(days, cell)
# 1부터 시작하기 때문에 1을 빼야 진짜 최소일이 나옴
print(days - 1)
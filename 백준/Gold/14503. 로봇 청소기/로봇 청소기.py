import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dir_y = [-1, 0, 1, 0]  # 북 동 남 서
dir_x = [0, 1, 0, -1]
cleaned_count = 0

while True:
    # 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2  # 청소된 곳은 2로 표시
        cleaned_count += 1

    moved = False
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 회전
        nr = r + dir_y[d]
        nc = c + dir_x[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc
            moved = True
            break

    if not moved:
        # 후진
        back_dir = (d + 2) % 4
        nr = r + dir_y[back_dir]
        nc = c + dir_x[back_dir]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
            r, c = nr, nc
        else:
            # 후진 불가 → 작동 멈춤
            print(cleaned_count)
            break

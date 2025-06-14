import sys

inp = int(sys.stdin.readline())

맵 = [['*' for _ in range(inp)] for _ in range(inp)]
def recursion(N, y, x):
    if N == 1:
        return
    after_n = N // 3
    for dy in range(3):
        for dx in range(3):
            ny = y + dy * after_n
            nx = x + dx * after_n
            # 가운데일 경우
            if dy == dx == 1:
                # 가운데 비우기
                for i in range(after_n):
                    for j in range(after_n):
                        맵[ny + i][nx + j] = ' '
            else:
                recursion(after_n, ny, nx)
recursion(inp, 0, 0)
for row in 맵:
    print(''.join(row))
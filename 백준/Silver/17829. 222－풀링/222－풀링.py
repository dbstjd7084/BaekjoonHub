import sys

N = int(sys.stdin.readline())

matrix = []

# 행렬값 받아오기
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# 두 번째로 큰 수 가져오기
def get2nd(matrix, matrix2):
    return sorted(matrix + matrix2)[-2]

# 222-풀링
def pulling(matrix):
    # N은 2의 거듭제곱임
    size = N
    while size > 1:
        # 222-풀링이 될 net_matrix
        new_matrix = []
        for y in range(0, size, 2):
            row = []
            for x in range(0, size, 2):
                row.append(sorted(matrix[y][x:x+2] + matrix[y+1][x:x+2])[-2])
            new_matrix.append(row)
        size//=2
        matrix = new_matrix
    else:
        print(matrix[0][0])

pulling(matrix)
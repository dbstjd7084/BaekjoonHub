import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())

DNA_List = [tuple(map(str, sys.stdin.readline().strip())) for _ in range(N)]
min_HD_str = ''
for i in range(M):
    # i번째 문자들을 모두 추출
    i_chars = [dna[i] for dna in DNA_List]
    # 각 문자별 등장 개수 추출
    counter = Counter(i_chars)
    most = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    min_HD_str += most[0][0]

print(min_HD_str)

count = 0
for i in range(N):
    for j in range(M):
        if DNA_List[i][j] != min_HD_str[j]:
            count += 1

print(count)
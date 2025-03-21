import sys
from collections import OrderedDict

# 최대 수강 인원 K, 대기목록 길이 L
K, L = map(int, sys.stdin.readline().split())

queue = OrderedDict()  # 순서 유지하며 중복 제거

# 대기목록 입력 처리
for _ in range(L):
    dept = sys.stdin.readline().strip()  # 개행 문자 제거
    if dept in queue:
        del queue[dept]  # 기존 학번 제거
    queue[dept] = True  # 최신 학번 추가

# K명 출력
for dept in list(queue.keys())[:K]:
    print(dept)
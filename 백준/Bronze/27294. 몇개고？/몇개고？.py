import sys

# 입력 받기, 수정이 필요없으므로 튜플 사용
T, S = tuple(map(int, sys.stdin.readline().split()))

# 점심시간이고 술이 없으면 320
if T >= 12 and T <= 16 and S == 0:
    print(320)
else:
    print(280)
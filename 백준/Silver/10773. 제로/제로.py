import sys
# 테스트 실행 횟수 입력받기
count = int(sys.stdin.readline())
total = 0
before = []
# 실행 횟수만큼 입력받기
for __ in range(count):
    inp = int(sys.stdin.readline())
    # 0이면 pop
    if (inp == 0):
        total-=before.pop()
    # 아니면 push 및 합 계산
    else:
        before.append(inp)
        total+=inp
print(total)
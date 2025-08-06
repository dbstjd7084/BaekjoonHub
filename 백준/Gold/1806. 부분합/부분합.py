from sys import stdin

N, S = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

부분합 = 0
start = 0
# S 이상의 부분합이 될 때까지 end 포인터 증가
for end_idx, end_value in enumerate(seq, 1):
    부분합 += end_value
    # 찾으면 탈출
    if 부분합 >= S:
        break
else:
    # 없으면 0 출력 및 중단
    print(0)
    exit()

# 부분합이 S 미만 될 때까지 start 포인터를 계속 증가시킴
while True:
    부분합 -= seq[start]
    start += 1
    # 만약 부분합이 S보다 작으면
    if 부분합 < S:
        # end 포인터의 idx(인덱스)가 끝에 도달한 경우 undo 후 탈출
        if end_idx == N:
            start -= 1
            break
        # end 포인터의 idx(인덱스)가 끝이 아닌 경우
        # end 포인터를 증가시킴
        부분합 += seq[end_idx]
        end_idx += 1

# 출력
print(end_idx - start)
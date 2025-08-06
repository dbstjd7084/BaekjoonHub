import sys

N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

end = 0
# 구하려는 길이 변수
length = 0
부분합 = 0

# 반복문 시작
for start in range(N):
    while 부분합 < S and end < N:
        # 부분합 구하기
        부분합 += seq[end]
        end += 1
    # S보다 크거나 같으면
    if 부분합 >= S:
        # length에 길이 저장
        # 만약 length에 이미 작은 값이 있다면 스킵
        if length > end - start or length == 0:
            length = end - start
    
    부분합 -= seq[start]

# 출력
print(length)
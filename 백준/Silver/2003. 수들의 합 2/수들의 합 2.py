import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

# 카운트 초기화
count = 0

# 찾는 함수(슬라이딩 윈도우): O(N)
def sumCount():
    global count
    start, end = 0, 0
    # start부터 end까지의 합 total
    total = 0
    while True:
        # 합이 찾는 값보다 같거나 크면 시작 포인트를 오른쪽으로 슬라이딩
        if total >= M:
            total -= A[start]
            start += 1
        # 합이 찾는 값보다 작고 end 포인터가 N이 되어 다시 처음으로 돌아갈 때 멈춤
        elif end == N:
            break
        # 합이 찾는 값보다 작다면 end 포인터를 오른쪽으로 슬라이딩딩 
        else:
            total += A[end]
            end += 1
        
        # 찾는 값이라면 count
        if total == M:
            count += 1

sumCount()
print(count)
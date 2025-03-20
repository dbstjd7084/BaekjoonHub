import sys

# 입력 받기
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

count = 0  # K번째 저장된 값을 추적하는 변수

def merge_sort(p, r):  
    if p < r:
        q = (p + r) // 2  # 중간 인덱스 계산
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)  # 병합 실행

def merge(p, q, r):
    global count
    i, j, t = p, q + 1, 0  
    tmp = [0] * (r - p + 1)  # 병합 결과를 저장할 리스트 (크기 미리 지정)

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:  # 왼쪽 배열의 남은 요소 저장
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:  # 오른쪽 배열의 남은 요소 저장
        tmp[t] = A[j]
        j += 1
        t += 1

    # 정렬된 내용을 원본 배열 A에 반영
    for t in range(r - p + 1):
        A[p + t] = tmp[t]
        count += 1
        if count == K:
            print(A[p + t])
            exit()  # K번째 저장된 값을 찾으면 즉시 종료

# 병합 정렬 실행
merge_sort(0, N - 1)

# K번째 저장이 발생하지 않으면 -1 출력
if (K > count):
    print(-1)
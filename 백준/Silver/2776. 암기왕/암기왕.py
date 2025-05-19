import sys

# 이분탐색 함수
def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)
    
# 입력 받기
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    수첩1 = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    수첩2 = list(map(int, sys.stdin.readline().split()))
    수첩1.sort()
        
    for target in 수첩2:
        print(binary_search(수첩1, target, 0, N - 1))
import sys

# N 입력 받기
N = int(sys.stdin.readline())
# A 입력 받기
A = list(map(int, sys.stdin.readline().split()))
# M 입력 받기
M = int(sys.stdin.readline())
# B 입력 받기기
B = list(map(int, sys.stdin.readline().split()))

# 오름차순 정렬
A.sort()

def BinarySearch(num):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == num:
            return 1
        elif A[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for i in B:
    print(BinarySearch(i))
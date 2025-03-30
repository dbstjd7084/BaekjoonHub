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

def BinarySearch(num, min, max):
    p = (min + max) // 2
    if A[p] == num:
        print(1)
    elif min + 1 == max:
        if A[p+1] == num:
            print(1)
        else:
            print(0)
    elif A[p] > num:
        BinarySearch(num, min, p)
    else:
        BinarySearch(num, p, max)

for i in B:
    BinarySearch(i, 0, len(A) - 1)
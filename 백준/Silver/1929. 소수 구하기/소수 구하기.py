import sys

M, N = map(int, sys.stdin.readline().split())

# 소수 구하기
def is_소수(num):
    arr = [True] * (num+1)
    arr[0] = False
    arr[1] = False
    half = num//2+1

    for i in range(2, half):
        if arr[i]:
            j = 2

            while i * j <= num:
                arr[i*j] = False
                j += 1
        
    return arr

소수들 = is_소수(N)

for i in range(M, N+1):
    if i >= M and 소수들[i]:
        print(i)
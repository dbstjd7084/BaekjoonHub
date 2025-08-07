import sys

N = int(sys.stdin.readline())

# 에라토스테네스의 체 알고리즘
def getPrimeNumbers(n):
    arr = [i for i in range(n+1)]
    arr[1] = 0
    # 루트n
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    # 소수만 반환
    return [x for x in arr if x != 0]

부분합 = 0
start = 0
end = 0
arr = getPrimeNumbers(N)
size = len(arr)
count = 0

while True:
    if 부분합 >= N:
        if 부분합 == N:
            count += 1
        부분합 -= arr[start]
        start += 1
    else:
        if end == size:
            break
        부분합 += arr[end]
        end += 1

print(count)
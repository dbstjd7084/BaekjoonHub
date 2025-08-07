import sys

N = int(sys.stdin.readline())

# 에라토스테네스의 체 알고리즘
def getPrimeNumbers(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

부분합 = 0
start = end = 0
arr = getPrimeNumbers(N)
size = len(arr)
count = 0

while True:
    if 부분합 >= N:
        if 부분합 == N:
            count += 1
        부분합 -= arr[start]
        start += 1
    elif end == size:
        break
    else:
        부분합 += arr[end]
        end += 1

print(count)
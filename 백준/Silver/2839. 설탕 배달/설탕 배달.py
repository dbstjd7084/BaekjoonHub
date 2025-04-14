import sys

N = int(sys.stdin.readline())

# N = 3 * A + 5 * B
# A + B 의 최솟값
# 유효한 A와 B값이라면, B가 가장 클 때 최솟값
B_max = N // 5
A = 0
B = 0
# B의 가능한 최댓값 B_max부터 1씩 내리면서 3의 배수인지 확인
# 3의 배수라면 A와 B 값을 설정
for i in range(B_max, -1, -1):
    mod = N - (5 * i)
    if mod % 3 == 0:
        B = i
        A = mod // 3
        print(A + B)
        break
# 만약 for문을 다 돌았는데도 결과가 없다면?
else:
    print(-1)
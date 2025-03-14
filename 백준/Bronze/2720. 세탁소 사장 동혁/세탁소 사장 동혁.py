# 첫째 줄값은 테스트 케이스 수 T
T = int(input())
# 입력값(거스름돈 액수)C 받아오기
for __ in range(T):
# 출력값에 따라 0.25, 0.1, 0.05, 0.01의 동전 개수 구하기
    C = int(input())
    q = 0
    d = 0
    n = 0
    p = 0
    while C >= 25:
        q += 1
        C -= 25
    while C >= 10:
        d += 1
        C -= 10
    while C >= 5:
        n += 1
        C -= 5
    while C >= 1:
        p += 1
        C -= 1
    print(q, d, n, p)
from sys import stdin

# 입력
N = stdin.readline()
용액 = list(map(int, stdin.readline().split()))
용액.sort()

start, end = 0, len(용액) - 1
# 가장 큰 양의 무한값 지정
가까운_합 = float('inf')
가까운_value = (None, None)

# 합이 0보다 작으면 start는 1씩 증가
# 아닐 시 end는 1씩 감소하면서 이동
# start 포인터와 end가 같아지면 종료됨 
while start < end:
    s = 용액[start] + 용액[end]

    if abs(s) < abs(가까운_합):
        가까운_합 = s
        가까운_value = (용액[start], 용액[end])

    if s < 0:
        start += 1
    else:
        end -= 1

print(가까운_value[0], 가까운_value[1])
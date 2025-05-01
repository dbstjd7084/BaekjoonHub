from collections import deque
import sys

dq = deque()

N = int(sys.stdin.readline())
for _ in range(N):
    parts = sys.stdin.readline().strip().split()
    
    if parts[0] == "push_front":
        dq.appendleft(int(parts[1]))  # 왼쪽에 값 추가
    elif parts[0] == "push_back":
        dq.append(int(parts[1]))  # 오른쪽에 값 추가
    elif parts[0] == "pop_front":
        if dq:
            print(dq.popleft())  # 왼쪽 값 제거 후 출력
        else:
            print(-1)  # 덱이 비었으면 -1 출력
    elif parts[0] == "pop_back":
        if dq:
            print(dq.pop())  # 오른쪽 값 제거 후 출력
        else:
            print(-1)  # 덱이 비었으면 -1 출력
    elif parts[0] == "size":
        print(len(dq))  # 덱의 크기 출력
    elif parts[0] == "empty":
        if len(dq) == 0:
            print(1)  # 덱이 비었으면 1 출력
        else:
            print(0)  # 덱이 비지 않았으면 0 출력
    elif parts[0] == "front":
        if dq:
            print(dq[0])  # 덱의 앞에 있는 값 출력
        else:
            print(-1)  # 덱이 비었으면 -1 출력
    elif parts[0] == "back":
        if dq:
            print(dq[-1])  # 덱의 뒤에 있는 값 출력
        else:
            print(-1)  # 덱이 비었으면 -1 출력

import sys

n = int(sys.stdin.readline())

birth = []

# 입력 받기
for _ in range(n):
    birth.append(tuple(sys.stdin.readline().split()))

# 가장 나이가 적은 사람 찾기
young = ()
for person in birth:
    if young == ():
        young = person
    # 년도가 더 어리다면 등록
    elif int(young[3]) < int(person[3]):
        young = person
    elif int(young[3]) == int(person[3]):
        # 달로 비교
        if int(young[2]) < int(person[2]):
            young = person
        elif int(young[2]) == int(person[2]):
            # 일로 비교
            if int(young[1]) < int(person[1]):
                young = person

old = ()
for person in birth:
    if old == ():
        old = person
    # 년도가 더 많다면면 등록
    elif int(old[3]) > int(person[3]):
        old = person
    elif int(old[3]) == int(person[3]):
        # 달로 비교
        if int(old[2]) > int(person[2]):
            old = person
        elif int(old[2]) == int(person[2]):
            # 일로 비교
            if int(old[1]) > int(person[1]):
                old = person

print(young[0])
print(old[0])
 # 분수찾기
# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> 1/3 -> 1/4

input = int(input())
# 1인 경우 기본값 출력
if (input == 1):
    print ("1/1")
else:
    count = 1
    while input > count*(count+1)/2:
        count+=1
    합 = count*(count+1)/2
    diff = 합 - input
    분모 = 1
    분자 = count

    if (count % 2 == 1):
        분모 = count - diff
        분자 = 1 + diff
    else:
        분자 = count - diff
        분모 = 1 + diff

    print(f"{int(분자)}/{int(분모)}")
input = int(input())
if (input == 1):
    print ("1/1")
else:
    count = 2
    while input > count*(count+1)/2:
        count+=1
    diff = count*(count+1)/2 - input
    if (count % 2 == 1):
        분모 = count - diff
        분자 = 1 + diff
    else:
        분자 = count - diff
        분모 = 1 + diff
    print(f"{int(분자)}/{int(분모)}")
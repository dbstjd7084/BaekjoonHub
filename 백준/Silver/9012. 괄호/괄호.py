import sys

for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().strip()
    if line[0] == ')':
        print("NO")
        continue
    else:
        count_괄호열기 = 0
        count_괄호닫기 = 0
        count_열린_상태 = 0
        for s in line:
            if s == '(':
                count_괄호열기 += 1
                count_열린_상태 += 1
            else:
                if (count_열린_상태 > 0):
                    count_괄호닫기 += 1
                    count_열린_상태 -= 1
                else:
                    print("NO")
                    break
        else:
            if count_괄호닫기 == count_괄호열기:
                print("YES")
            else:
                print("NO")
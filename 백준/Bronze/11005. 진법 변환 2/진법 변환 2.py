# N과 B진법 가져오기
N, B = map(int, input().split())
# 함수 선언
def trans(v):
    if v == 10:
        return "A"
    elif v == 11:
        return "B"
    elif v == 12:
        return "C"
    elif v == 13:
        return "D"
    elif v == 14:
        return "E"
    elif v == 15:
        return "F"
    elif v == 16:
        return "G"
    elif v == 17:
        return "H"
    elif v == 18:
        return "I"
    elif v == 19:
        return "J"
    elif v == 20:
        return "K"
    elif v == 21:
        return "L"
    elif v == 22:
        return "M"
    elif v == 23:
        return "N"
    elif v == 24:
        return "O"
    elif v == 25:
        return "P"
    elif v == 26:
        return "Q"
    elif v == 27:
        return "R"
    elif v == 28:
        return "S"
    elif v == 29:
        return "T"
    elif v == 30:
        return "U"
    elif v == 31:
        return "V"
    elif v == 32:
        return "W"
    elif v == 33:
        return "X"
    elif v == 34:
        return "Y"
    elif v == 35:
        return "Z"
    else:
        return v
# N을 B진법으로 변환
count = 0
while N >= B**(count+1):
    count += 1
out = ""
while count >= 0:
    out += str(trans(N % B))
    N //= B
    count -= 1
print(out[::-1])
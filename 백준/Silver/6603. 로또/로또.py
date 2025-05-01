import sys

while True:

    inputs = list(map(int, input().split()))

    k = inputs[0]
    S = inputs[1:]

    if (inputs[0] == 0):
        break

    def find(S, start, current, k):
        if len(current) == 6:
            print(*current)
            return

        for i in range(start, len(S)):
            current.append(S[i])
            find(S, i + 1, current, k)
            current.pop()

    find(S, 0, [], k)
    print("")
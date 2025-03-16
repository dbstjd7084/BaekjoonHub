count = int(input())
stack = []
for __ in range(count):
    inp = int(input())
    if (inp == 0):
        stack.pop()
    else:
        stack.append(inp)
sum = 0
if stack.count == 0:
    print(0)
else:
    for i in range(len(stack)):
        sum+=stack[i]

    print(sum)
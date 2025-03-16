count = int(input())
stack = []
for __ in range(count):
    inp = int(input())
    if (inp == 0):
        stack.pop()
    else:
        stack.append(inp)
print(sum(stack))
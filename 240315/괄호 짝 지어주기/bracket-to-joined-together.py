input_val = input()
stack = []
cnt = 0
for element in input_val:
    if element == '(':
        stack.append('(')
    elif stack:
        stack.pop()
    else:
        stack.append('(')
        cnt += 1

print(cnt + (len(stack)//2))
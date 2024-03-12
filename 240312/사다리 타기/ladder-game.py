n, m = map(int, input().split())
line_state = [[0] * (n+1) for _ in range(16)]
lines = []
found = False

for _ in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))
    line_state[b][a] = 1


def return_result(arr):
    ref = []
    for j in range(1, n+1):
        num = j
        for i in range(1, 16):
            if arr[i][num-1]:
                num -= 1
            elif arr[i][num]:
                num += 1

        ref.append(num)
    return ref

def choose_lines(level, limit, start):
    global found
    if level == limit:
        new_result = return_result(new_line_state)
        if ref == new_result:
            found = True
        return
    
    for i in range(start, m):
        a, b = lines[i]
        new_line_state[b][a] = 1
        choose_lines(level+1, limit, i+1)
        new_line_state[b][a] = 0


ref = return_result(line_state)
if ref == list(range(1, n+1)):
    print(0)
else:
    new_line_state = [[0] * (n+1) for _ in range(16)]
    for i in range(1, m):
        choose_lines(0, i, 0)
        if found:
            print(i)
            break
    else:
        print(m)
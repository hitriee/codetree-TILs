def int_input():
    return map(int, input().split())

def can_pass(now, before, length, to_bottom):
    break_flag = False
    if now == before:
        length += 1
    elif now == before - 1:
        if to_bottom:
            if length < L:
                break_flag = True
        else:
            to_bottom = True
        length = 1
    elif now == before + 1:
        if to_bottom:
            if length < 2*L:
                break_flag = True
            to_bottom = False
        else:
            if length < L:
                break_flag = True
            length = 1
    else:
        break_flag = True
    
    return (length, to_bottom, break_flag)


N, L = int_input()
heights = [list(int_input()) for _ in range(N)]
total_cnt = 0

for i in range(N):
    before, length = heights[i][0], 1
    to_bottom = False
    for j in range(1, N):
        now = heights[i][j]
        length, to_bottom, break_flag = can_pass(now, before, length, to_bottom)
        if break_flag:
            break
        before = now
    else:
        if not to_bottom or length >= L:
            total_cnt += 1

for j in range(N):
    before, length = heights[0][j], 1
    to_bottom = False
    for i in range(1, N):
        now = heights[i][j]
        length, to_bottom, break_flag = can_pass(now, before, length, to_bottom)
        if break_flag:
            break
        before = now
    else:
        if not to_bottom or length >= L:
            total_cnt += 1

print(total_cnt)
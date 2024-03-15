input_val = input()
n = len(input_val)
cnt = close_cnt = 0

for element in input_val:
    if element == ')':
        close_cnt += 1

def cnt_correct(level, red, blue, left):
    global cnt

    if red > left or blue > left:
        return

    if level == n:
        cnt += 1
        return
    
    element = input_val[level]
    if element == '(':
        cnt_correct(level+1, red+1, blue, left)
        cnt_correct(level+1, red, blue+1, left)
    else:
        if red > 0:
            cnt_correct(level+1, red-1, blue, left-1)
        if blue > 0:
            cnt_correct(level+1, red, blue-1, left-1)

cnt_correct(0, 0, 0, close_cnt)

print(cnt%2012)
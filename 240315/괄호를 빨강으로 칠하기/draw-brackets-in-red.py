input_val = input()
n = len(input_val)
cnt = 0

def cnt_correct(level, red, blue):
    global cnt

    if level == n:
        if red == 0 and blue == 0:
            cnt += 1
        return
    
    element = input_val[level]
    if element == '(':
        cnt_correct(level+1, red+1, blue)
        cnt_correct(level+1, red, blue+1)
    else:
        if red > 0:
            cnt_correct(level+1, red-1, blue)
        if blue > 0:
            cnt_correct(level+1, red, blue-1)

cnt_correct(0, 0, 0)

print(cnt%2012)
A = input()
open_cnt = close_cnt = cnt = 0
for element in A:
    if element == '(':
        cnt += 1
        if cnt == 2:
            open_cnt += 1
            cnt -= 1
    else:
        cnt = 0


cnt = 0
for element in A:
    if element == ')':
        cnt += 1
        if cnt == 2:
            close_cnt += 1
            cnt -= 1
    else:
        cnt = 0

print(open_cnt * close_cnt)
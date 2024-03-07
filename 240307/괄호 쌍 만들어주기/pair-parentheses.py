A = input()
n = len(A)
close_cnt = cnt = total_cnt = 0
is_open = False
info = []
for i in range(n-1, -1, -1):
    element = A[i]
    if is_open:
        if element == '(':
            cnt += 1
        else:
            total_cnt += (cnt - 1) * close_cnt
            cnt = 1
            is_open = False
    elif element == ')':
        cnt += 1
    else:
        close_cnt += (cnt - 1)
        cnt = 1
        is_open = True

if is_open:
    total_cnt += (cnt - 1) * close_cnt

print(total_cnt)
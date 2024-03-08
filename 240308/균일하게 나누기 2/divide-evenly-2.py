from sys import stdin

new_input = stdin.readline
N = int(new_input())
x_to_y, right_y_cnt = {}, {}
for _ in range(N):
    x, y = map(int, new_input().split())
    if x_to_y.get(x):
        x_to_y[x].append(y)
    else:
        x_to_y[x] = [y]

    if right_y_cnt.get(y):
        right_y_cnt[y] += 1
    else:
        right_y_cnt[y] = 1

sorted_x = sorted(x_to_y)
sorted_y = sorted(right_y_cnt)
len_x, len_y = len(sorted_x), len(sorted_y)
min_max_cnt = N
bottom_cnt = left_cnt = 0
left_y_cnt = {}

for i in range(len_x-1):
    x = sorted_x[i]
    left_cnt += len(x_to_y[x])
    for y in x_to_y[x]:
        if left_y_cnt.get(y):
            left_y_cnt[y] += 1
        else:
            left_y_cnt[y] = 1
        
        right_y_cnt[y] -= 1

    b_l_cnt = b_r_cnt = 0

    for j in range(len_y-1):
        y = sorted_y[j]
        b_l_cnt += left_y_cnt.get(y, 0)
        b_r_cnt += right_y_cnt.get(y, 0)
        max_cnt = max(b_l_cnt, left_cnt - b_l_cnt, b_r_cnt, N - left_cnt - b_r_cnt)
        
        if min_max_cnt > max_cnt:
            min_max_cnt = max_cnt
        

print(min_max_cnt)
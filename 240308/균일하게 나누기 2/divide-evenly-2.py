from sys import stdin

new_input = stdin.readline
N = int(new_input())
x_to_y, right_y_cnt, left_y_cnt = {}, {}, {}

for _ in range(N):
    x, y = map(int, new_input().split())
    x_to_y[x] = x_to_y.get(x, []) + [y]
    right_y_cnt[y] = right_y_cnt.get(y, 0) + 1

sorted_x, sorted_y = sorted(x_to_y), sorted(right_y_cnt)
len_y = len(sorted_y)
min_max_cnt, left_cnt = N, 0

for x in sorted_x:
    b_l_cnt = b_r_cnt = 0
    left_cnt += len(x_to_y[x])

    for y in x_to_y[x]:
        left_y_cnt[y] = left_y_cnt.get(y, 0) + 1
        right_y_cnt[y] -= 1


    for j in range(len_y-1):
        y = sorted_y[j]
        b_l_cnt += left_y_cnt.get(y, 0)
        b_r_cnt += right_y_cnt.get(y, 0)
        max_cnt = max(b_l_cnt, left_cnt - b_l_cnt, b_r_cnt, N - left_cnt - b_r_cnt)
        
        if min_max_cnt > max_cnt:
            min_max_cnt = max_cnt
        

print(min_max_cnt)
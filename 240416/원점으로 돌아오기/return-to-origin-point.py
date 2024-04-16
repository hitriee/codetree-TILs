N = int(input())
cnt = 0
dots = [tuple(map(int, input().split())) for _ in range(N)]
visited = [False] * N

def find_new_i(y, x, dot_y, dot_x):
    if dot_y == y:
        return 0 if dot_x > x else 1
    elif dot_x == x:
        return 2 if dot_y > y else 3
    return -1

def cnt_case(level, y, x, i):
    global cnt
    if level == N:
        new_i = find_new_i(y, x, 0, 0)
        if new_i >= 0 and new_i != i:
            cnt += 1
        return
    
    for j in range(N):
        if not visited[j]:
            dot_y, dot_x = dots[j]
            new_i = find_new_i(y, x, dot_y, dot_x)

            if new_i >= 0 and new_i != i:
                visited[j] = True
                cnt_case(level+1, dot_y, dot_x, new_i)
                visited[j] = False

for j in range(N):
    y, x = dots[j]
    new_i = find_new_i(0, 0, y, x)
    if new_i >= 0:
        visited[j] = True
        cnt_case(1, y, x, new_i)
        visited[j] = False

print(cnt)
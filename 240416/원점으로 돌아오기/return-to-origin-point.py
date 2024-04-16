N = int(input())
cnt = 0
dots = [tuple(map(int, input().split())) for _ in range(N)]
visited = [False] * N
dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]

def cnt_case(level, y, x, i):
    global cnt
    if level == N:
        if y == 0 or x == 0:
            cnt += 1
        return
    
    for j in range(N):
        if not visited[j]:
            dot_y, dot_x = dots[j]
            visited[j] = True
            if dot_y == y:
                if dot_x > x:
                    if i != 0:
                        cnt_case(level+1, y, dot_x, 0)
                elif i != 1:
                    cnt_case(level+1, y, dot_x, 1)
            elif dot_x == x:
                if dot_y > y:
                    if i != 2:
                        cnt_case(level+1, dot_y, x, 2)
                elif i != 4:
                    cnt_case(level+1, dot_y, x, 4)
            
            visited[j] = False


cnt_case(0, 0, 0, -1)
print(cnt)
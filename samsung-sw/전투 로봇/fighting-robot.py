from collections import deque

def find_position():
    cnt = 0
    for i in range(N):
        for j in range(N):
            level = board[i][j]
            if level == 9:
                position = (i, j)
                board[i][j] = 0
            elif level > 0:
                monsters[level].append((i, j))
                cnt += 1

    for i in range(1, 7):
        monsters[i].sort()
    
    return (cnt, *position)


def bfs(r, c, level):
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    q = deque()
    q.append((r, c, 0))
    final_y, final_x, min_val = -1, -1, N*N
    while q:
        y, x, time = q.popleft()
        if 0 < board[y][x] < level:
            if time < min_val:
                final_y, final_x, min_val = y, x, time
            elif time == min_val:
                if y < final_y:
                    final_y, final_x = y, x
                elif y == final_y and x < final_x:
                    final_x = x
            else:
                break
        else:
            new_time = time + 1
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx]:
                        val = board[ny][nx]
                        if val <= level:
                            visited[ny][nx] = True
                            q.append((ny, nx, new_time))
    
    if final_y != -1:
        already[final_y][final_x] = True
        board[final_y][final_x] = 0
        return (final_y, final_x, min_val)
    return (-1, -1, -1)




N = int(input())
# 1 ~ 6 몬스터의 레벨 / 9 전투 로봇
board = [list(map(int, input().split())) for _ in range(N)]
# 일을 끝내기 전까지 걸린 시간
dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)

monsters = [[] for _ in range(7)]
M, y, x = find_position()
total_time, level, cnt, start = 0, 2, 0, 1
already = [[False] * N for _ in range(N)]

for _ in range(M):
    y, x, time = bfs(y, x, level)
    if time < 0:
        break
    cnt += 1
    if cnt == level:
        level += 1
        cnt = 0
    
    total_time += time

print(total_time)


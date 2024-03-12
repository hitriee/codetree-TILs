from collections import deque

N, M = map(int, input().split())
area = [input().split() for _ in range(N)]
visited_time = [[-1] * M for _ in range(N)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
q = deque()

def in_area(y, x, value, time):
    if 0 <= y < N and 0 <= x < M:
        if visited_time[y][x] == -1 and area[y][x] == value:
            visited_time[y][x] = time
            return True
    return False

def fill_q():
    temp = deque()
    q.append((0, 0, 0))
    temp.append((0, 0))
    
    while temp:
        y, x = temp.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if in_area(ny, nx, '0', 0):
                q.append((ny, nx, 0))
                temp.append((ny, nx))

def melt_ice():
    while q:
        y, x, time = q.popleft()
        time += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if in_area(ny, nx, '1', time):
                q.append((ny, nx, time))

    return time-1

def find_last_size(time):
    size = 0
    for i in range(N):
        for j in range(M):
            if visited_time[i][j] == time:
                size += 1
    return size


fill_q()
# print(visited_time)
last_time = melt_ice()

# print(*visited_time)

print(last_time, find_last_size(last_time))
from collections import deque

N, M = map(int, input().split())
area = [input().split() for _ in range(N)]
empty, fire, walls = [], [], []

for i in range(N):
    for j in range(M):
        val = area[i][j]
        if val == '2':
            fire.append((i, j))
        elif val == '0':
            empty.append((i, j))
        else:
            walls.append((i, j))

L, K = len(empty), len(fire)
q = deque()
max_cnt = 0
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)


def choose(level, start):
    if level == 3:
        cnt = spread()
        return
    
    for i in range(start, L):
        y, x = empty[i]
        area[y][x] = '1'
        choose(level+1, i+1)
        area[y][x] = '0'


def spread():
    global max_cnt

    new_area = [area[i][:] for i in range(N)]
    q.extend(fire)
    cnt = len(empty) - 3

    while True:
        need_break = True
        temp = []
        while q:
            y, x = q.popleft()
            temp.append((y, x))
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if new_area[ny][nx] == '0':
                        new_area[ny][nx] = '2'
                        q.append((ny, nx))
                        need_break = False
                        cnt -= 1


        if need_break:
            break
        
        q.extend(temp)

    if cnt > max_cnt:
        max_cnt = cnt

choose(0, 0)

print(max_cnt)
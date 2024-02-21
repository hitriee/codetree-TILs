N, M, Q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
minus_one = lambda x: int(x)-1

def move(r1, c1, r2, c2):
    y, x, i = r1, c1, 0
    edge_length = 2 * (r2 - r1 + c2 - c1) - 1
    edge = [building[r1][c1]]

    for _ in range(edge_length):
        ny, nx = y+dy[i], x+dx[i]
        if r1 <= ny <= r2 and c1 <= nx <= c2:
            y, x = ny, nx
        else:
            i += 1
            y, x = y+dy[i], x+dx[i]
        
        edge.append(building[y][x])

    y, x, i = r1, c1, 0
    building[r1][c1] = edge[-1]

    for j in range(edge_length):
        ny, nx = y+dy[i], x+dx[i]
        if r1 <= ny <= r2 and c1 <= nx <= c2:
            y, x = ny, nx
        else:
            i += 1
            y, x = y+dy[i], x+dx[i]
        
        building[y][x] = edge[j]
    

def change(r1, c1, r2, c2):
    result = [[] for _ in range(r2 - r1 + 1)]
    
    for y in range(r1, r2+1):
        for x in range(c1, c2+1):
            cnt, total = 1, building[y][x]
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    cnt += 1
                    total += building[ny][nx]
            result[y-r1].append(total//cnt)
    
    for y in range(r1, r2+1):
        for x in range(c1, c2+1):
            building[y][x] = result[y-r1][x-c1]
    

for _ in range(Q):
    wind_info = tuple(map(minus_one, input().split()))
    move(*wind_info)
    change(*wind_info)

for i in range(N):
    print(*building[i])
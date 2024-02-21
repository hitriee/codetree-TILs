N, M, Q = map(int, input().split())
building = [input().split() for _ in range(N)]
reversed_d = {'R':'L', 'L':'R'}

def move_each(r, d):
    if d == 'R':
        start, end, step = 0, M-1, 1
    else:
        start, end, step = M-1, 0, -1
    
    temp = building[r][start]

    for j in range(start, end, step):
        building[r][j] = building[r][j+step]
    
    building[r][end] = temp

def move(r, d):
    r = int(r) - 1
    move_each(r, d)

    for start, end, step in (r-1, -1, -1), (r+1, N, 1):
        new_d = d
        for i in range(start, end, step):
            new_d = reversed_d[new_d]
            for j in range(M):
                if building[i-step][j] == building[i][j]:
                    move_each(i, new_d)
                    break
            else:
                break

for _ in range(Q):
    move(*input().split())

for i in range(N):
    print(' '.join(building[i]))
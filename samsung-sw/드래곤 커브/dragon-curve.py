def make_curve(y, x, d, g):
    ny, nx = y+dy[d], x+dx[d]
    arr[y][x] = True
    line = [(y, x, d)]
    r, c = ny, nx

    for _ in range(g):
        m = len(line)
        temp = []
        for i in range(m-1, -1, -1):
            j = (line[i][-1] + 1) % 4
            nr, nc = r+dy[j], c+dx[j]
            arr[r][c] = True
            temp.append((r, c, j))
            r, c = nr, nc
        
        arr[r][c] = True
        line.extend(temp)


def count_rectangle():
    cnt = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if can_link(i, j):
                cnt += 1

    return cnt

def can_link(i, j):
    for di in range(-1, 1):
        for dj in range(-1, 1):
            ni, nj = i+di, j+dj
            if not arr[ni][nj]:
                return False
    return True


N = int(input())
arr = [[False] * 101 for _ in range(101)]
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

for _ in range(N):
    make_curve(*map(int, input().split()))
    

print(count_rectangle())



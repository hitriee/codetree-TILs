from sys import stdin
from collections import deque

def int_input():
    return map(int, stdin.readline().split())

def in_range(y, x):
    return 0 <= y < R+3 and 1 <= x < C+1

def can_move(i, r, c):
    for j in around_idx[i]:
        nr, nc = r+dr[j], c+dc[j]
        if not in_range(nr, nc) or forest[nr][nc] != 0:
            return False
        
        for k in range(4):
            nnr, nnc = nr+dr[k], nc+dc[k]
            if not in_range(nnr, nnc) or forest[nnr][nnc] != 0:
                return False
        r, c = nr, nc
    return True

def initiate():
    for i in range(R+3):
        for j in range(1, C+1):
            forest[i][j] = 0

def move_all(idx, r, c, d):
    forest[r][c] = idx
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        forest[nr][nc] = idx
    forest[r+dr[d]][c+dc[d]] = -idx


def move_inside(idx, r, c):
    max_r = r
    q = deque()
    visited = [[False] * (C+1) for _ in range(R+3)]
    q.append((idx, r, c))
    visited[r][c] = True
    while q:
        num, y, x = q.popleft()
        if max_r < y:
            max_r = y
        for i in range(4):
            ny, nx = y+dr[i], x+dc[i]
            if in_range(ny, nx) and not visited[ny][nx]:
                new_num = forest[ny][nx]
                if (num < 0 and new_num != 0) or (abs(num) == abs(new_num)):
                    q.append((new_num, ny, nx))
                    visited[ny][nx] = True
    return max_r

def find_row(idx, c, d):
    r = 1
    while True:
        for i in range(3):
            if can_move(i, r, c):
                for j in around_idx[i]:
                    r += dr[j]
                    c += dc[j]
                d += delta_arr[i]
                break
        else:
            break
    
    if r <= 3:
        initiate()
        return 2
    
    d %= 4
    
    move_all(idx, r, c, d)
    return move_inside(idx, r, c)


R, C, K = int_input()
forest = [[0] * (C+1) for _ in range(R+3)]
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
around_idx = [(2,), (3, 2), (1, 2)]
delta_arr = [0, -1, 1]
total = 0
for idx in range(1, K+1):
    total += find_row(idx, *int_input()) - 2

print(total)

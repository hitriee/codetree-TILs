from collections import deque

def int_input():
    return map(int, input().split())

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def roll_dice(idx):
    new_dice_info = list(dice_info)

    new_dice_info[0] = dice_info[idx+1]
    
    new_idx = idx % 2 + 1
    conf = idx % 2
    new_dice_info[new_idx] = dice_info[-1] if idx == conf else dice_info[0]
    
    for i in range(3):
        dice_info[i] = new_dice_info[i]
    for i in range(3, 5):
        dice_info[i] = 7 - new_dice_info[i-2]
    dice_info[-1] = 7 - new_dice_info[0]

def change_idx(idx, y, x):
    bottom, val = dice_info[0], board[y][x]
    if bottom > val:
        return (idx+1) % 4
    if bottom < val:
        return (idx-1) % 4
    return idx

def calc_score(y, x):
    target = board[y][x]
    visited = [[False] * N for _ in range(N)]
    q = deque()
    visited[y][x] = True
    cnt = 1
    q.append((y, x))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dy[i], c+dx[i]
            if in_range(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc] == target:
                    q.append((nr, nc))
                    cnt += 1
    
    return target * cnt



def move(idx, y, x):
    ny, nx = y+dy[idx], x+dx[idx]
    if not in_range(ny, nx):
        idx = (idx-2) % 4
        ny, nx = y+dy[idx], x+dx[idx]
    
    score = calc_score(ny, nx)
    roll_dice(idx)
    idx = change_idx(idx, ny, nx)

    return score, idx, ny, nx

N, M = int_input()
board = [list(int_input()) for _ in range(N)]
y = x = total = idx = 0
dice_info = [6, 3, 2, 4, 5, 1]
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

for _ in range(M):
    score, idx, y, x = move(idx, y, x)
    total += score

print(total)
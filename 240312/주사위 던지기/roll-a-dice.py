n, m, r, c = map(int, input().split())
r -= 1
c -= 1
arr = [[0] * m for _ in range(n)]
dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
direction_to_idx = {'U':0, 'L':1, 'D':3, 'R':2}
commands = input().split()
total = down = 6
arr[r][c] = 6
around = [5, 4, 3, 2]

def in_arr(y, x):
    return 0 <= y < n and 0 <= x < n

for command in commands:
    idx = direction_to_idx[command]
    nr, nc = r+dr[idx], c+dc[idx]
    if in_arr(nr, nc):
        total -= arr[nr][nc]
        down, around[idx], around[3-idx] = around[idx], 7-down, down
        arr[nr][nc] = down
        r, c = nr, nc
        total += down

print(total)
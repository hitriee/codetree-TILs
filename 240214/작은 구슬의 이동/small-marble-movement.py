n, t = map(int, input().split())
r, c, d = input().split()
r, c = map(int, [r, c])
direction = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3,
}
dy, dx = [-1, 0, 0, 1], [0, 1, -1, 0]
direct_idx = direction[d]
now = 0

for now in range(1, t+1):
    nr, nc = r + dy[direct_idx], c + dx[direct_idx]
    if 1 <= nr <= n and 1 <= nc <= n:
        r, c = nr, nc
    else:
        direct_idx = 3 - direct_idx

print(r, c)
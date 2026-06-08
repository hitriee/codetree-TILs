from collections import deque

def int_input(func=int):
    return map(func, input().split())

def minus_one(num):
    return int(num) - 1

N, K = int_input()
arr = [list(int_input()) for _ in range(N)]

r1, c1 = int_input(minus_one)
r2, c2 = int_input(minus_one)

visited = [[[False] * (K+1) for _ in range(N)] for _ in range(N)]

q = deque()
dr, dc = (-1, 0, 1, 0), (0, -1, 0, 1)
q.append((r1, c1, 0, 0))
visited[r1][c1][0] = True

while q:
    r, c, time, chance = q.popleft()
    if r == r2 and c == c2:
        print(time)
        break
    
    new_time = time + 1
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            new_chance = chance + arr[nr][nc]
            if new_chance <= K and not visited[nr][nc][new_chance]:
                visited[nr][nc][new_chance] = True
                q.append((nr, nc, new_time, new_chance))

else:
    print(-1)
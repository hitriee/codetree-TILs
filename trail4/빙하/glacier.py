from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)
water, ice = deque(), deque()
water.append((0, 0))
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
duration = last_size = 0

def melt():
    while water:
        y, x = water.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if a[ny][nx] == 1:
                        ice.append((ny, nx))
                    else:
                        water.append((ny, nx))
    water.extend(ice)
    ice.clear()



while True:
    melt()
    length = len(water)
    if length == 0:
        break
    
    last_size = length
    duration += 1
    


print(duration, last_size)
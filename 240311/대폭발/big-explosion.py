n, m, r, c = map(int, input().split())
r -= 1
c -= 1
arr = [[False] * n for _ in range(n)]
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
arr[r][c] = True

def can_add_dynamite(y, x):
    if 0 <= y < n and 0 <= x < n and not arr[y][x]:
        arr[y][x] = True
        return True
    return False

def cnt_dynamite():
    cnt = distance = 1
    now = [(r, c)]
    for _ in range(m):
        before = now[:]
        for y, x in before:
            for i in range(4):
                ny, nx = y+dy[i]*distance, x+dx[i]*distance
                if can_add_dynamite(ny, nx):
                    now.append((ny, nx))
                    cnt += 1
                
        distance *= 2
    
    return cnt

print(cnt_dynamite())
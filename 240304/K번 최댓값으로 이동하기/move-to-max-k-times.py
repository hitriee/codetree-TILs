from collections import deque

n, k = map(int, input().split()) # 크기, 반복 횟수
arr = [list(map(int, input().split())) for _ in range(n)] # 격자 정보
r, c = map(lambda x: int(x)-1, input().split()) # 초기 위치
dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]
q = deque()

def can_move(y, x, ref): # 범위 안 & 기준 숫자보다 작음 & 방문 X
    if 0 <= y < n and 0 <= x < n and arr[y][x] < ref and not visited[y][x]:
        visited[y][x] = True
        return True
    return False

def move():
    visited[r][c] = True
    q.append((r, c))
    ref, num = arr[r][c], 0
    final = ()
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if can_move(ny, nx, ref):
                value = arr[ny][nx]
                if num < value:
                    final = (ny, nx)
                    num = value
                elif num == value:
                    if final[0] > ny or (final[0] == ny and final[1] > nx):
                        final = (ny, nx)
                        num = value
                q.append((ny, nx))
    
    return final
        
for _ in range(k):
    visited = [[False] * n for _ in range(n)]
    result = move()
    if result:
        r, c = result
    else:
        break

print(f'{r+1} {c+1}')
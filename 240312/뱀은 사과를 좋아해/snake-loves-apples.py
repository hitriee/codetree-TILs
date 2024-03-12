from collections import deque

N, M, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]
snake_body = deque([(0, 0)])
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
direct_to_idx = {'U': 0, 'L': 1, 'D': 2, 'R': 3}
convert = lambda x: int(x) if x.isdigit() else direct_to_idx[x]

arr[0][0] = -1
for _ in range(M):
    y, x = map(lambda x: int(x)-1, input().split())
    arr[y][x] = 1

def calc_time():
    time = 0
    for j in range(K):
        idx, num = map(convert, input().split())
        for _ in range(num):
            time += 1
            y, x = snake_body[0]
            ny, nx = y+dy[idx], x+dx[idx]

            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] != 1:
                    last_y, last_x = snake_body.pop()
                    arr[last_y][last_x] = 0
                    
                    if arr[ny][nx] == -1:
                        if last_y != ny or last_x != nx:
                            return time
                
                snake_body.appendleft((ny, nx))
                arr[ny][nx] = -1
            else:
                return time

    return time

print(calc_time())
from collections import deque
L, N, Q = map(int, input().split())
board = [input().split() for _ in range(L)]
position = [[-1] * L for _ in range(L)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
knights = []
total = 0


# 이동 가능한지 여부
def can_move(num, d):

    # 데이터 추가
    def append_data(idx):
        visited[idx] = True
        r, c, h, w, _ = knights[idx]
        for y in range(r, r+h):
            for x in range(c, c+w):
                ny, nx = y+dy[d], x+dx[d]
                q.append((ny, nx))
        # print(idx, q)

    q = deque()
    visited = [False] * N
    append_data(num)
    
    while q:
        # print(q)
        y, x = q.popleft()
        if 0 <= y < L and 0 <= x < L:
            # print(y,x, board[y][x], position[y][x])
            # 이동할 곳에 벽이 있으면 이동 불가
            if board[y][x] == '2':
                return False
            
            # 이동할 곳에 다른 기사가 존재하면 q에 추가
            new_idx = position[y][x]
            if new_idx != -1:
                if not visited[new_idx]:
                    append_data(new_idx)
        
        # 보드판 벗어나면 이동 불가
        else:
            return False
    
    return True


# 이동 # 대미지
def move(num, d):
    # 데이터 추가 & 배치 변경
    def append_data(idx):
        cnt = 0
        visited[idx] = True
        path = []
        r, c, h, w, _ = knights[idx]
        for y in range(r, r+h):
            for x in range(c, c+w):
                ny, nx = y+dy[d], x+dx[d]
                path.append((ny, nx))
                q.append((ny, nx))
                if board[ny][nx] == '1':
                    cnt += 1
        

        knights[idx][-1] -=  cnt
        if knights[idx][-1] > 0:
            for y, x in path:
                new_position[y][x] = idx

        return cnt


    damage = 0
    q = deque()
    visited = [False] * N
    new_position = [[-1] * L for _ in range(L)]
    append_data(num)

    while q:
        y, x = q.popleft()
        # 이동할 곳에 다른 기사가 존재하면 q에 추가
        new_idx = position[y][x]
        if new_idx != -1 and not visited[new_idx]:
            damage += append_data(new_idx)

    for i in range(N):
        if not visited[i]:
            r, c, h, w, _ = knights[i]
            for y in range(r, r+h):
                for x in range(c, c+w):
                    new_position[y][x] = position[y][x]
        else:
            for y in range(L):
                for x in range(L):
                    if new_position[y][x] == i:
                        knights[i][:2] = [y, x]
                        break


    for i in range(L):
        position[i] = new_position[i][:]
    


    return damage

for i in range(N):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    knights.append([r, c, h, w, k])
    for y in range(r, r+h):
        for x in range(c, c+w):
            position[y][x] = i

for _ in range(Q):
    i, d = map(int, input().split())
    # 체력이 0이 아니면 이동 가능한지 확인
    if knights[i-1][-1] > 0 and can_move(i-1, d):
        total += move(i-1, d)

print(total)
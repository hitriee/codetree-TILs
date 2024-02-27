n = int(input())
if n == 1:
    print(2)
else:
    arr = [input().split() for _ in range(n)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    y = x = i = max_time = 0

    def pinball(r, c, d):
        time = 0
        while True:
            time += 1
            if arr[r][c] == '1':
                d = 3 - d
            elif arr[r][c] == '2':
                if d%2:
                    d -= 1
                else:
                    d += 1
            
            nr, nc = r+dy[d], c+dx[d]
            if 0 <= nr < n and 0 <= nc < n:
                r, c = nr, nc
                continue
            
            return time+1


    while True:
        time = pinball(y, x, (i+1)%4)
        if max_time < time:
            max_time = time
        
        ny, nx = y+dy[i], x+dx[i]
        if ny == nx == 0:
            break
        
        if 0 <= ny < n and 0 <= nx < n:
            y, x = ny, nx
        else:
            i += 1
            if i == 4:
                break
            y += dy[i]
            x += dx[i]
        
    print(max_time)
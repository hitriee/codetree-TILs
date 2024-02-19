n, m = map(int, input().split())
area = [input().split() for _ in range(n)]
cost = [i*i + (i+1)*(i+1) for i in range(n+1)]
max_cnt = 0
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

for y in range(n):
    for x in range(n):
        each_cnt, gold_cnt = 1, 0
        visited = [[False] * n for _ in range(n)]
        visited[y][x] = True
        if area[y][x] == '1':
            gold_cnt += 1
            if max_cnt == 0:
                max_cnt = 1
        edge, temp = [(y, x)], []
        for k in range(1, n+1):
            for ny, nx in edge:
                for i in range(4):
                    nny, nnx = ny+dy[i], nx+dx[i]
                    if 0 <= nny < n and 0 <= nnx < n and not visited[nny][nnx]:
                        visited[nny][nnx] = True
                        temp.append((nny, nnx))
                        if area[nny][nnx] == '1':
                            gold_cnt += 1
            if max_cnt < gold_cnt and gold_cnt * m >= cost[k]:
                max_cnt = gold_cnt
            if not temp:
                break
            edge, temp = temp[:], []

print(max_cnt)
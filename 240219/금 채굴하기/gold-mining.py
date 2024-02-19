n, m = map(int, input().split())
area = [input().split() for _ in range(n)]
max_cnt = 0
max_num = max(n, m)
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

for y in range(n):
    for x in range(m):
        each_cnt, gold_cnt = 1, 0
        if area[y][x] == '1':
            gold_cnt += 1
            if max_cnt == 0:
                max_cnt = 1
        
        for k in range(1, max_num):
            new_gold_cnt = gold_cnt
            for ny in range(max(0, y-k+1), min(y+k, n)):
                for nx in range(max(0, x-k+1), min(x+k, m)):
                    each_cnt += 1
                    if area[ny][nx] == '1':
                        gold_cnt += 1

            for i in range(4):
                ny, nx = y + dy[i] * k, x + dx[i] * k
                if 0 <= ny < n and 0 <= nx < m:
                    each_cnt += 1
                    if area[ny][nx] == '1':
                        new_gold_cnt += 1
            
            if new_gold_cnt * m >= each_cnt and max_cnt < new_gold_cnt:
                max_cnt = new_gold_cnt

print(max_cnt)
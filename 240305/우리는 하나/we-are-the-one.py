from collections import deque

n, k, u, d = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
results = [['']*n for _ in range(n)]
q = deque()
max_cnt = 0
square = n*n

def conf_results(result1, result2):
    new_result = ''
    for i in range(square):
        if result1[i] == result2[i] == '0':
            new_result += '0'
        else:
            new_result += '1'
    
    return new_result


def can_travel(y, x, ref):
    if 0 <= y < n and 0 <= x < n and u <= abs(ref - cities[y][x]) <= d:
        return True
    return False

def travel(*initial):
    q.append(initial)
    while q:
        y, x = q.popleft()
        ref = cities[y][x]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            idx = ny*n+nx
            if can_travel(ny, nx, ref) and check[idx] == '0':
                check[idx] = '1'
                q.append((ny, nx))

def choose_cites(level, start, result):
    global max_cnt

    if level == k:
        cnt = str(result).count('1')
        if max_cnt < cnt:
            max_cnt = cnt
        return
    
    for i in range(start, square):
        quot, remain = divmod(i, n)
        new_result = conf_results(result, results[quot][remain])
        choose_cites(level+1, i+1, new_result)


for i in range(n):
    for j in range(n):
        check = ['0'] * square
        check[i*n+j] = '1'
        q.append((i, j))
        travel(i, j)
        results[i][j] = ''.join(check)

choose_cites(0, 0, '0'*square)

print(max_cnt)
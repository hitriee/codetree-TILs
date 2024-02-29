N = int(input())
arr = [input() for _ in range(N)]
S, E = (), ()
coin_list = [() for _ in range(10)]
min_cnt = 22*N

for i in range(N):
    for j in range(N):
        value = arr[i][j]
        if value.isdigit():
            coin_list[int(value)] = (i, j)
        elif value == 'S':
            S = (i, j)
        elif value == 'E':
            E = (i, j)

def calc_distance(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

def choose_coin(level, cnt, before, start):
    global min_cnt

    if level == 3:
        cnt += calc_distance(*before, *E)
        if min_cnt > cnt:
            min_cnt = cnt
        return
    
    for i in range(start, 10):
        coin = coin_list[i]
        if coin:
            choose_coin(level+1, cnt+calc_distance(*before, *coin), coin, i+1)


choose_coin(0, 0, S, 0)

if min_cnt < 22*N:
    print(min_cnt)
else:
    print(-1)
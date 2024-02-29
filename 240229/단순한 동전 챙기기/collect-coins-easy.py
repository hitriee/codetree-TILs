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

for i in range(8):
    coin1 = coin_list[i]
    if coin1:
        cnt1 = calc_distance(*S, *coin1)
        if cnt1 < min_cnt:
            for j in range(i+1, 9):
                coin2 = coin_list[j]
                if coin2:
                    cnt2 = cnt1 + calc_distance(*coin1, *coin2)
                    if cnt2 < min_cnt:
                        for k in range(j+1, 10):
                            coin3 = coin_list[k]
                            if coin3:
                                cnt3 = cnt2 + calc_distance(*coin2, *coin3) + calc_distance(*coin3, *E)
                                if min_cnt > cnt3:
                                    min_cnt = cnt3

if min_cnt < 22*N:
    print(min_cnt)
else:
    print(-1)
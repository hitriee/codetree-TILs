# 이동
def move():
    after_move = []
    for y in range(N):
        for x in range(N):
            for m, s, d in arr[y][x]:
                ny, nx = (y + s * dy[d]) % N, (x + s * dx[d]) % N
                after_move.append((ny, nx, m, s, d))
            arr[y][x] = []

    for ny, nx, m, s, d in after_move:
        arr[ny][nx].append((m, s, d))

# 합성
def combine():
    for y in range(N):
        for x in range(N):
            info = arr[y][x]
            length = len(info)
            if length >= 2:
                nm, ns = info[0][0], info[0][1]
                remain, is_straight = info[0][2] % 2, True
                for i in range(1, length):
                    m, s, d = info[i]
                    nm += m
                    ns += s
                    if is_straight and d % 2 != remain:
                        is_straight = False
                
                if nm >= 5:
                    nm //= 5
                    ns //= length
                    start = 0 if is_straight else 1
                    arr[y][x] = [(nm, ns, nd) for nd in range(start, 8, 2)]
                else:
                    arr[y][x] = []

def calc_total():
    total = 0
    for y in range(N):
        for x in range(N):
            for m, _, _ in arr[y][x]:
                total += m
    return total



def int_input():
    return map(int, input().split())

N, M, K = int_input()
dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, m, s, d = int_input()
    y -= 1
    x -= 1
    arr[y][x].append((m, s, d))

for _ in range(K):
    move()
    combine()

print(calc_total())
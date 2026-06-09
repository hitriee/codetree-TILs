# 이동
def move():
    after_move = []
    for y, x in atoms:
        for m, s, d in arr[y][x]:
            ny, nx = (y + s * dy[d]) % N, (x + s * dx[d]) % N
            after_move.append((ny, nx, m, s, d))
    
    atoms.clear()
    for i in range(N):
        for j in range(N):
            arr[i][j].clear()

    for ny, nx, m, s, d in after_move:
        arr[ny][nx].append((m, s, d))
        atoms.add((ny, nx))

# 합성
def combine():
    new_total = total

    before = set(atoms)
    for y, x in before:
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
            
            new_total -= nm
            if nm >= 5:
                nm //= 5
                new_total += 4*nm
                ns //= length
                start = 0 if is_straight else 1
                arr[y][x] = [(nm, ns, nd) for nd in range(start, 8, 2)]
            else:
                atoms.remove((y, x))
                arr[y][x] = []
    
    return new_total



def int_input():
    return map(int, input().split())

N, M, K = int_input()
dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
arr = [[[] for _ in range(N)] for _ in range(N)]
atoms = set()
total = 0

for _ in range(M):
    y, x, m, s, d = int_input()
    y -= 1
    x -= 1
    arr[y][x].append((m, s, d))
    atoms.add((y, x))
    total += m

for _ in range(K):
    move()
    total = combine()

print(total)
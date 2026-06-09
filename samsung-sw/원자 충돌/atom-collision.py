# 이동
def move():
    temp_set, temp_arr = set(), [[[] for _ in range(N)] for _ in range(N)]

    for y, x in atoms:
        for m, s, d in arr[y][x]:
            ny, nx = (y + s * dy[d]) % N, (x + s * dx[d]) % N
            temp_set.add((ny, nx))
            temp_arr[ny][nx].append((m, s, d))
    
    return temp_set, temp_arr

# 합성
def combine():
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
            
            if nm >= 5:
                nm //= 5
                ns //= length
                start = 0 if is_straight else 1
                arr[y][x] = [(nm, ns, nd) for nd in range(start, 8, 2)]
            else:
                atoms.remove((y, x))
                arr[y][x] = []
    


# 질량의 합
def calc_total():
    total = 0
    for y, x in atoms:
        for m, _, _ in arr[y][x]:
            total += m
    return total


def int_input():
    return map(int, input().split())

N, M, K = int_input()
dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
arr = [[[] for _ in range(N)] for _ in range(N)]
atoms = set()

for _ in range(M):
    y, x, m, s, d = int_input()
    y -= 1
    x -= 1
    arr[y][x].append((m, s, d))
    atoms.add((y, x))

for _ in range(K):
    atoms, arr = move()
    # print('m', atoms, arr)
    combine()
    # print('c', atoms, arr)

print(calc_total())

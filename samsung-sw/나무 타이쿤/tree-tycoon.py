N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
dy, dx = (0, -1, -1, -1, 0, 1, 1, 1), (1, 1, 0, -1, -1, -1, 0, 1)
position = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]
visited = [[False] * N for _ in range(N)]
length = 4


def move(d, p):
    d -= 1
    for i in range(length):
        y, x = position[i]
        ny, nx = (y + p * dy[d]) % N, (x + p * dx[d]) % N
        position[i] = (ny, nx)


def grow():
    delta = []
    for y, x in position:
        area[y][x] += 1

    for y, x in position:
        cnt = 0
        for i in range(1, 8, 2):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and area[ny][nx] >= 1:
                cnt += 1
        area[y][x] += cnt
        visited[y][x] = True
    
    position.clear()


def create():
    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                visited[y][x] = False
            elif area[y][x] >= 2:
                area[y][x] -= 2
                position.append((y, x))


def sum_height():
    total = 0
    for y in range(N):
        total += sum(area[y])
    return total


for _ in range(M):
    # d : 이동 방향 (1 ~ 8), p : 이동 칸 수
    # 특수 영양제 이동
    move(*map(int, input().split()))

    # 투입한 리브로수 기존 높이 + (대각선으로 인접한 방향에 높이가 1 이상인 리브로수 개수)
    grow()
    # 특수 영양제를 투입한 리브로수 제외하고 높이가 2 이상인 리브로수는 높이 2를 베어서 특수 영양제 올려둠
    create()
    length = len(position)

print(sum_height())

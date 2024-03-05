n = int(input())
area = [input().split() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
cnt = 0
people = []

def can_count(y, x):
    if 0 <= y < n and 0 <= x < n and area[y][x] == '1' and not visited[y][x]:
        visited[y][x] = True
        return True
    return False

def count_town(y, x):
    global headcount

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if can_count(ny, nx):
            headcount += 1
            count_town(ny, nx)



for i in range(n):
    for j in range(n):
        if area[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            headcount = 1
            count_town(i, j)
            cnt += 1
            people.append(headcount)

people.sort()
print(cnt, *people, sep='\n')
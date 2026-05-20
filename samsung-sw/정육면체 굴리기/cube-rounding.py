def minus_one(num):
    return int(num) - 1

def roll_dice():
    ny, nx = y+dy[d], x+dx[d]
    if 0 <= ny < N and 0 <= nx < M:
        dice[d], dice[1^d], dice[4], dice[5] = dice[5], dice[4], dice[d], dice[1^d]
        next_val = map_info[ny][nx]
        if next_val == 0:
            map_info[ny][nx] = dice[5]
        else:
            dice[5], map_info[ny][nx] = next_val, 0
        
        return (ny, nx)

N, M, y, x, k = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(minus_one, input().split()))
dy, dx = (0, 0, -1, 1), (1, -1, 0, 0)
# 동 / 서 / 북 / 남 / 위 / 아래
dice = [0] * 6

for d in directions:
    new_position = roll_dice()
    if new_position:
        y, x = new_position
        print(dice[-2])

    

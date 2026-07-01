from sys import stdin

# i 번 줄의 결과는 무조건 i번으로 가야 함
# 최소한의 선을 추가해 버그 없애기
def minus_one(num):
    return int(num) - 1

def int_input(func=int):
    return map(func, stdin.readline().split())

def choose(level, start):
    global min_cnt

    if level == min_cnt:
        return
    
    if check():
        min_cnt = level
        return

    
    new_level = level + 1
    for idx in range(start, limit):
        i, j = divmod(idx, N-1)
        if not has_line[i][j]:
            if i < N-1 and has_line[i][j+1]:
                continue
            if i > 0 and has_line[i][j-1]:
                continue
            has_line[i][j] = True
            choose(new_level, idx+1)
            has_line[i][j] = False


def check():
    for j in range(N):
        col = j
        for row in range(H):
            if has_line[row][col]:
                col += 1
            elif col > 0 and has_line[row][col-1]:
                col -= 1
        if col != j:
            return False
    return True
        
    
    


N, M, H = int_input()
has_line = [[False] * N for _ in range(H)]
min_cnt, limit = 4, (N-1) * H

for _ in range(M):
    a, b = int_input(minus_one)
    has_line[a][b] = True

choose(0, 0)

print(min_cnt if min_cnt < 4 else -1)

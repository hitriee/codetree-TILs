n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
min_dif = 1000
half = n // 2
path = []
visited = [False] * (1<<21)

def backtracking(level, start, score1, now):
    global min_dif

    if visited[now]:
        return

    visited[now] = True

    if level == half:
        new_path = []
        remain = score2 = 0
        for i in range(n):
            state = 1 << i
            if now & state == 0:
                for j in new_path:
                    score2 += table[i][j] + table[j][i]
                remain += state
                new_path.append(i)
                
        
        visited[remain] = True
        dif = abs(score1 - score2)
        if dif < min_dif:
            min_dif = dif

        return
    
    for i in range(start, n):
        new_score = score1
        for j in path:
            new_score += table[i][j] + table[j][i]
        future = now + (1 << i)
        path.append(i)
        backtracking(level+1, i+1, new_score, future)
        path.pop()
        
    




backtracking(0, 0, 0, 0)

print(min_dif)
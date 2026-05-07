n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
min_dif = 1000
half = n // 2
now = 0
path = []
visited = set()

def backtracking(level, start, score1):
    global min_dif, now

    if level == half:
        if now in visited:
            return
        
        new_path = []
        remain = score2 = 0
        for i in range(n):
            state = 1 << i
            if now & state == 0:
                for j in new_path:
                    score2 += table[i][j] + table[j][i]
                remain += state
                new_path.append(i)
                
        
        visited.add(now)
        visited.add(remain)

        dif = abs(score1 - score2)
        if dif < min_dif:
            min_dif = dif

        return
    
    for i in range(start, n):
        new_score = score1
        for j in path:
            new_score += table[i][j] + table[j][i]
        now += 1 << i
        path.append(i)
        backtracking(level+1, i+1, new_score)
        now -= 1 << i
        path.pop()
        
    




backtracking(0, 0, 0)

print(min_dif)
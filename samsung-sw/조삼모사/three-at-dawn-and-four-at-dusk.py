n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
min_dif = 1000
half = n // 2
path = []

def backtracking(level, start, score):
    global min_dif

    if level == half:
        new_path = []
        idx = remain = 0
        for i in range(n):
            if idx >= half or path[idx] != i:
                for j in new_path:
                    remain += table[i][j] + table[j][i]
                new_path.append(i)
            else:
                idx += 1
        dif = abs(score - remain)
        if dif < min_dif:
            min_dif = dif

        return
    
    for i in range(start, n):
        new_score = score
        for j in path:
            new_score += table[i][j] + table[j][i]
        path.append(i)
        backtracking(level+1, i+1, new_score)
        path.pop()
        
    




backtracking(0, 0, 0)

print(min_dif)
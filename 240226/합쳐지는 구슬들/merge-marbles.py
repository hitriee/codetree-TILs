n, m, t = map(int, input().split())
arr = [[-1] * n for _ in range(n)]
converted_d = {'U': 1, 'D': 2, 'R': 0, 'L': 3}
dr, dc, position = [0, -1, 1, 0], [1, 0, 0, -1], []
cnt = max_w = 0

def convert(x):
    return converted_d[x] if x.isalpha() else int(x)

for i in range(m):
    r, c, d, w = map(convert, input().split())
    position.append([r-1, c-1, d, w])
    arr[r-1][c-1] = [i]

for _ in range(t):
    new_arr = [[-1] * n for _ in range(n)]
    for i in range(m):
        if position[i]:
            r, c, d, w = position[i]
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                r, c = nr, nc
                before_i = new_arr[r][c]

                if before_i != -1:
                    w += position[before_i][-1]
                    position[before_i] = ()
                
                position[i] = [nr, nc, d, w]

            else:
                position[i][2] = 3-d
            
            new_arr[r][c] = i
            

    arr = [new_arr[i][:] for i in range(n)]

for i in range(m):
    if position[i]:
        cnt += 1
        if max_w < position[i][-1]:
            max_w = position[i][-1]

print(cnt, max_w)
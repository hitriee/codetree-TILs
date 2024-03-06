n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(n)]
a_comb, b_comb = [[''] * 3 for _ in range(n)], [['']*3 for _ in range(n)]
cnt = 0

def find_comb(level, start):
    global cnt

    if level == 3:
        a_set = set(''.join(a_comb[i]) for i in range(n))
        b_set = set(''.join(b_comb[i]) for i in range(n))
        
        for a_str in a_set:
            if a_str in b_set:
                break
        else:
            cnt += 1
        return
    
    for i in range(start, m):
        for j in range(n):
            a_comb[j][level] = a[j][i]
            b_comb[j][level] = b[j][i]
        find_comb(level+1, i+1)

find_comb(0, 0)
print(cnt)
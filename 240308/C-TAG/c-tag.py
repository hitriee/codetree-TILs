from sys import stdin

new_input = stdin.readline
n, m = map(int, new_input().split())
a = [new_input().rstrip() for _ in range(n)]
b = [new_input().rstrip() for _ in range(n)]
path = []
cnt = 0

def find_comb(level, start):
    global cnt

    if level == 3:
        a_comb, b_comb = set(), set()
        for i in range(n):
            a_result = b_result = ''
            for j in path:
                a_result += a[i][j]
                b_result += b[i][j]
            a_comb.add(a_result)
            b_comb.add(b_result)
        
        for a_str in a_comb:
            if a_str in b_comb:
                break
        else:
            cnt += 1
        return
    
    for i in range(start, m):
        path.append(i)
        find_comb(level+1, i+1)
        path.pop()

find_comb(0, 0)
print(cnt)
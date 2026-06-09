from sys import stdin

new_input = stdin.readline

N, Q = map(int, new_input().split())
arr = [int(new_input()) - 1 for _ in range(N)]
cnt = [[0] * 3 for _ in range(N+3)]

for i in range(N):
    for j in range(3):
        cnt[i+1][j] = cnt[i][j]
    cnt[i+1][arr[i]] += 1

for _ in range(Q):
    a, b = map(int, new_input().split())
    answer = [str(cnt[b][j] - cnt[a-1][j]) for j in range(3)]
    print(' '.join(answer))
    

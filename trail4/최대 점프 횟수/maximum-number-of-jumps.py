N = int(input())
arr = list(map(int, input().split()))
cnt = [0] * N

# Please write your code here.
for i in range(N-1):
    if i == 0 or cnt[i] != 0:
        limit = min(N, i + arr[i]+1)
        for j in range(i+1, limit):
            cnt[j] = max(cnt[i] + 1, cnt[j])

print(max(cnt))
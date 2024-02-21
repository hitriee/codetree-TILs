n = int(input())
zenga = [input() for _ in range(n)]

for _ in range(2):
    s, e = map(int, input().split())
    j = s-1
    for i in range(e, n):
        zenga[j] = zenga[i]
        j += 1
    n -= (e - s + 1)

print(n)

for i in range(n):
    print(zenga[i])
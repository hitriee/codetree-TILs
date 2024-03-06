from heapq import heappush, heappop
n, m = map(int, input().split())
dots = []

for _ in range(n):
    x, y = map(int, input().split())
    heappush(dots, (x+y, x, y))

for _ in range(m):
    val, x, y = heappop(dots)
    x += 2
    y += 2
    heappush(dots, (val+4, x, y))

print(*dots[0][1:])
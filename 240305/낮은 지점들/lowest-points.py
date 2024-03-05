n = int(input())
dots = {}
limit = 2e9
for _ in range(n):
    x, y = map(int, input().split())
    if dots.get(x, limit) > y:
        dots[x] = y
print(sum(dots.values()))
n = int(input())
dots = {}
for _ in range(n):
    x, y = map(int, input().split())
    if not dots.get(x) or dots[x] > y:
        dots[x] = y
print(sum(dots.values()))
n, q = map(int, input().split())
points = list(map(int, input().split()))
point_to_idx = {points[i]: i for i in range(n)}

for _ in range(q):
    a, b = map(int, input().split())
    print(point_to_idx[b] - point_to_idx[a] + 1)

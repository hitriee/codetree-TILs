from sys import stdin

def int_input():
    return map(int, stdin.readline().split())

n, q = int_input()
points = list(int_input())
point_to_idx = {points[i]: i for i in range(n)}

for _ in range(q):
    a, b = int_input()
    print(point_to_idx[b] - point_to_idx[a] + 1)

from heapq import heappush, heappop

n = int(input())
maxheap = []

for _ in range(n):
    x = int(input())
    if x:
        heappush(maxheap, -x)
    elif maxheap:
        print(-heappop(maxheap))
    else:
        print(0)
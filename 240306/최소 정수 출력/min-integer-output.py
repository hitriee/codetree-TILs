from heapq import heappush, heappop

n = int(input())
minheap = []

for _ in range(n):
    x = int(input())
    if x:
        heappush(minheap, x)
    else:
        print(heappop(minheap) if minheap else 0)
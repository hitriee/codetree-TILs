from heapq import heappush, heappop

n = int(input())
minheap = []

for _ in range(n):
    x = int(input())
    if x:
        heappush(minheap, x)
    elif minheap:
        print(heappop(minheap))
    else:
        print(0)
from heapq import heappush, heappop, heapify

abs_heap = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        heappush(abs_heap, (abs(x), x))
    elif abs_heap:
        _, min_num = heappop(abs_heap)
        print(min_num)
    else:
        print(0)
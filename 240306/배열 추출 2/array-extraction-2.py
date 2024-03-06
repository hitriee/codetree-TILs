from heapq import heappush, heappop, heapify

abs_heap = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(abs_heap, (x, x))
    elif x < 0:
        heappush(abs_heap, (-x, x))
    elif abs_heap:
        min_num = heappop(abs_heap)[1]
        print(min_num)
    else:
        print(0)
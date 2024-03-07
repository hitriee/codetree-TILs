from heapq import heappush, heappop

n, m, k = map(int, input().split())
numbers1 = sorted(map(int, input().split()))
numbers2 = sorted(map(int, input().split()))
max_heap = []
need_break = False
cnt = 0

for num1 in numbers1:
    for num2 in numbers2:
        minus_total = -(num1+num2)
        if cnt < k:
            cnt += 1
            heappush(max_heap, minus_total)
        elif max_heap[0] < minus_total:
            heappop(max_heap)
            heappush(max_heap, minus_total)
        else:
            break

print(-max_heap[0])
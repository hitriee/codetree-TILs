from heapq import heappush, heappop

n, m, k = map(int, input().split())
numbers1 = sorted(map(int, input().split()))
numbers2 = sorted(map(int, input().split()))
max_heap = []
cnt = 0

for num1 in numbers1:
    for num2 in numbers2:
        minus_total = -(num1+num2)
        if cnt < k:
            cnt += 1
        elif max_heap[0] < minus_total:
            heappop(max_heap)
        else:
            break
        heappush(max_heap, minus_total)

print(-max_heap[0])
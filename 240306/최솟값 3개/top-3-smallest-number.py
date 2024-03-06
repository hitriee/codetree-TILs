from heapq import heappush, heappop

n = int(input())
numbers = tuple(map(int, input().split()))
max_heap = []
result = -1

def multiple_three(num1, num2, num3):
    return -(num1 * num2 * num3)

for i in range(n):
    number = -numbers[i]
    heappush(max_heap, number)
    if i >= 3:
        max_num = heappop(max_heap)
        if max_num != number:
            result = multiple_three(*max_heap)
    elif i == 2:
        result = multiple_three(*max_heap)

    
    print(result)
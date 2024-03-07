from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    m = int(input())
    numbers = list(map(int, input().split()))
    result = numbers[:1]
    mid_num = result[0]
    smaller, larger = [], []
    
    for i in range(1, m):
        number = numbers[i]
        if number >= mid_num:
            heappush(larger, number)
        else:
            heappush(smaller, -number)
        
        if i%2 == 0:
            len_l, len_s = len(larger), len(smaller)
            
            if len_l > len_s:
                for _ in range((len_l - len_s)//2):
                    heappush(smaller, -mid_num)
                    mid_num = heappop(larger)
            
            elif len_l < len_s:
                for _ in range((len_s - len_l)//2):
                    heappush(larger, mid_num)
                    mid_num = -heappop(smaller)
            
            result.append(mid_num)
    
    print(*result)
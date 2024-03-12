N = int(input())

def make_N():
    from collections import deque
    q = deque()
    q.append((1, 0))
    limit = int(1e6)

    while q:
        num, cnt = q.popleft()
        if num == N:
            return cnt
        num_set = set()
        if num < limit:
            num_set.add(num+1)
        if num > 1:
            num_set.add(num-1)
        num_set.add(num*2)
        num_set.add(num*3)
        
        cnt += 1
        for new_num in num_set:
            q.append((new_num, cnt))

print(make_N())
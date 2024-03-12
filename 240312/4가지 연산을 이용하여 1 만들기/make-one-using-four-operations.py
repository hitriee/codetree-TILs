N = int(input())
limit = int(1e6)+1

def return_four(num):
    new_nums = []
    if num < limit-1:
        new_nums.append(num+1)
    if num > 1:
        new_nums.append(num-1)
    if num % 2 == 0:
        new_nums.append(num//2)
    if num % 3 == 0:
        new_nums.append(num//3)
    
    return new_nums


def make_one():
    from collections import deque
    q = deque()
    visited = [False] * limit
    q.append((N, 0))
    visited[N] = True

    while q:
        num, cnt = q.popleft()
        if num == 1:
            return cnt
        
        cnt += 1
        new_nums = return_four(num)
        for new_num in new_nums:
            if not visited[new_num]:
                visited[new_num] = True
                q.append((new_num, cnt))

print(make_one())
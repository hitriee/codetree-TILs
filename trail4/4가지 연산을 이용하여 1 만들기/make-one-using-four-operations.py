N = int(input())


# Please write your code here.
def bfs():
    from collections import deque

    limit = 2 * N
    min_cnt = [limit] * limit

    q = deque()
    min_cnt[1] = 0
    q.append((1, 0))

    while q:
        num, cnt = q.popleft()
        if num == N:
            return cnt

        new_cnt = cnt + 1

        for new_num in (num + 1, num - 1, num * 2, num * 3):
            if 0 <= new_num < limit and min_cnt[new_num] > new_cnt:
                min_cnt[new_num] = new_cnt
                q.append((new_num, new_cnt))


print(bfs())